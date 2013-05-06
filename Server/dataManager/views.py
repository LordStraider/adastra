from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from dataManager.models import UploadFileForm, Menu, DropDown, Content
from django.utils import simplejson
from django.conf import settings
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
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
    return render(request, 'index.html', {'form': form}, context_instance=RequestContext(request))


def save_file(file, path):
    fd = open(path, 'w+b')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()


def index(request, site=''):
    return render_to_response('index.html', context_instance=RequestContext(request))


def album(request, subSite=''):
    return render_to_response('gallery.html')


def siteContent(request, site=''):
    item = Content.objects.get(site=site)
    string = '{"siteContent": "' + item.text + '"}'
    input_map = simplejson.loads(string, strict=False)
    return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')


def fileLoader(request, site=''):
    imageAlbum = Content.objects.get(site=site).text.split(', ')
    string = '[{"title": "' + imageAlbum.pop(0) + '"}, {"path": "' + settings.STATIC_URL + 'images/albums/endagistallet/"}, '
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
