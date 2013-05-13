from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from dataManager.models import UploadFileForm, Menu, DropDown, Content
from django.contrib.auth.views import login as auth_login
from django.utils import simplejson
from django.conf import settings
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
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


def index(request, site=''):
    return render_to_response('index.html')


@csrf_protect
def admin_index(request, site=''):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate(username='Admin', password='barbapapa')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('adminIndex.html', context_instance=RequestContext(request))
    return render_to_response('login.html', context_instance=RequestContext(request))


@csrf_protect
def submitMenu(request):
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
    print request.POST.items()[0][0]
    js = simplejson.loads(request.POST.items()[0][0])
    print js
    text = js.get('text')
    site = js.get('site')
    obj = Content.objects.get(site=site)
    obj.text = text
    obj.save()
    return HttpResponse(True)


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
    string = '[{"title": "' + imageAlbum.pop(0) + '"}, {"path": "' + settings.STATIC_URL + 'images/albums/endagtallet/"}, '
    for image in imageAlbum:
        string += '{"fileLoader": "' + image + '"}, '
    string += 'end'
    string = string.split(", end")[0] + ']'
    input_map = simplejson.loads(string, strict=False)
    return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')


def menu(request):
    if request.is_ajax():
        string = '['
        for item in Menu.objects.all():
            string += '{"menu": "' + item.text + '", "subs": ['
            for sub in DropDown.objects.filter(Menu=item):
                string += '{"sub": "' + sub.text + '", "linked": "' + sub.link
                if sub.hasFiles:
                    string += '/fileLoader'
                string += '"}, '
            string += 'end'
            string = string.split(", end")[0].split("end")[0] + '], "linked": "' + item.link + '"}, '
        string += 'end'
        string = string.split(", end")[0] + ']'
        input_map = simplejson.loads(string)
        return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')
