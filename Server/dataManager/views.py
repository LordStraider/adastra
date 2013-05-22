from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from dataManager.models import UploadFileForm, Menu, DropDown, Content
from django.contrib.auth.views import login as auth_login
from django.utils import simplejson
from django.conf import settings
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os


@csrf_protect
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            site = "stallet"
            filename = request.FILES['file']._get_name()
            path = '%s' % ('static/images/albums/endagistallet/' + filename)
            if not os.path.isfile(path):
                a = open(path, 'w')
                a.close()
            save_file(request.FILES['file'], path)
            album = Content.objects.get(site=site)
            album.text += (", " + request.POST['title'] + ":" + filename)
            album.save()
            return render_to_response('index.html', context_instance=RequestContext(request))
    else:
        form = UploadFileForm()
    return render(request, 'adminIndex.html', {'form': form}, context_instance=RequestContext(request))


def save_file(file, path):
    fd = open(path, 'w+b')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()


@csrf_protect
def upload_files(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html', context_instance=RequestContext(request))
    import re

    chars = [',', ':', '!', ';', '?']

    if request.method == 'POST':
        if request.is_ajax():
            newString = ''
            for file in request.FILES.getlist('files[]'):
                path = '%s' % ('static/images/albums/endagistallet/' + re.sub('[%s]' % ''.join(chars), '', file.name))
                destination = open(path, 'w+b')
                for chunk in file.read():
                    destination.write(chunk)
                destination.close()

                newString += re.sub('[%s]' % ''.join(chars), '', file.name) + ':' + re.sub('[%s]' % ''.join(chars), '', file.name) + ', '
            newString = newString[:-2]

            title = re.sub('[%s]' % ''.join(chars), '', request.POST.get('title'))
            string = title + ', '
            toggle = True
            for destination in request.POST.getlist('file'):
                string += re.sub('[%s]' % ''.join(chars), '', destination)
                if toggle:
                    string += ':'
                else:
                    string += ', '
                toggle = not toggle

            if newString == '':
                string = string[:-2]
            else:
                string += newString

            site = request.POST.get('site')
            obj = Content.objects.get(site=site)
            obj.text = string
            obj.save()

            if newString != '':
                json = '{"newFile": "True", "path": "/static/images/albums/endagistallet/", "file": "' + newString + '"}'
            else:
                json = '{"newFile": "False"}'

            return HttpResponse(json)
        return HttpResponse('{"error": "not ajax."}')
    return HttpResponse('{"error": "not post."}')


def index(request, site=''):
    return render_to_response('index.html')


@csrf_protect
def admin_index(request, site=''):
    if request.user.username == 'Straider' and request.user.is_authenticated():
        return render_to_response('adminIndex.html', context_instance=RequestContext(request))
    return render_to_response('login.html', context_instance=RequestContext(request))


@csrf_protect
def submitMenu(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html', context_instance=RequestContext(request))

    js = simplejson.loads(request.POST.items()[0][0])
    text = js.get('text')
    link = js.get('link')
    if js.get('site'):
        DropDown.create(Menu.objects.get(link=js.get('site')), text, link, False)
    else:
        Menu.create(text, link)
    Content.create(text, link)
    return HttpResponse(True)


@csrf_protect
def submitContent(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html', context_instance=RequestContext(request))
    print request.POST.items()
    js = simplejson.loads(request.POST.items()[0][0])
    text = js.get('text')
    site = js.get('site')
    album = js.get('isAlbum')
    if album:
        dropDown = DropDown.objects.get(link=site)
        dropDown.hasFiles = True
        dropDown.save()
    obj = Content.objects.get(site=site)
    obj.text = text
    obj.save()
    return HttpResponse(True)


@csrf_protect
def logout(request):
    logout(request.user)
    return HttpResponse(True)


def checkLoggedIn(request):
    if request.user.is_authenticated():
        string = '{"loggedIn": "True", "firstName": "' + request.user.first_name + '", "lastName": "' + request.user.last_name + '"}'
    else:
        string = '{"loggedIn": "False"}'
    input_map = simplejson.loads(string, strict=False)
    return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')


def siteContent(request, site=''):
    item = Content.objects.get(site=site)
    string = '{"admin": false, "siteContent": "' + item.text + '"}'
    input_map = simplejson.loads(string, strict=False)
    return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')


def siteAdminContent(request, site=''):
    item = Content.objects.get(site=site)
    string = '{"admin": true, "siteContent": "' + item.text + '"}'
    input_map = simplejson.loads(string, strict=False)
    return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')


def fileLoader(request, site=''):
    imageAlbum = Content.objects.get(site=site).text.split(', ')
    string = '[{"title": "' + imageAlbum.pop(0) + '"}, {"path": "' + settings.STATIC_URL + 'images/albums/endagistallet/"}, '
    for image in imageAlbum:
        string += '{"fileLoader": "' + image + '"}, '
    string = string[:-2]+ ']'
    input_map = simplejson.loads(string, strict=False)
    return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')


def menu(request):
    if request.is_ajax():
        string = '['
        for item in Menu.objects.all():
            string += '{"menu": "' + item.text + '", "subs": [  '
            for sub in DropDown.objects.filter(Menu=item):
                string += '{"sub": "' + sub.text + '", "linked": "' + sub.link
                if sub.hasFiles:
                    string += '/fileLoader'
                string += '"}, '
            string = string[:-2] + '], "linked": "' + item.link + '"}, '
        string = string[:-2] + ']'
        input_map = simplejson.loads(string)
        return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')
