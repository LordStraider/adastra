from django.shortcuts import render_to_response
from django.http import HttpResponse
from dataManager.models import Menu, DropDown, Content
from django.utils import simplejson


def index(request, subSite=''):
    return render_to_response('index.html')


def siteContent(request, site=''):
    item = Content.objects.get(site=site)
    string = '{"siteContent": "' + item.text + '"}'
    input_map = simplejson.loads(string, strict=False)
    return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')


def menu(request):
    if request.is_ajax():
        string = '['
        for item in Menu.objects.all():
            string += '{"menu": "' + item.text + '", "subs": ['
            for sub in DropDown.objects.filter(Menu=item):
                string += '{"sub": "' + sub.text + '", "linked": "' + sub.link + '"}, '
            string += 'end'
            string = string.split(", end")[0].split("end")[0] + '], "linked": "' + item.link + '"}, '
        string += 'end'
        string = string.split(", end")[0] + ']'
        input_map = simplejson.loads(string)
        return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')


def gallery(request):
    return render_to_response('gallery.html')


def galleryContent(request):
    #galleryObj = Gallery.objects.all()
    #gallery = galleryObj[0]
    #string = '{"galleryContent": "' + gallery.text + '"}'
    #input_map = simplejson.loads(string, strict=False)
    #return HttpResponse(simplejson.dumps(input_map), mimetype='application/javascript')
    return HttpResponse(simplejson.dumps({"galleryContent": "this is the gallery page."}), mimetype='application/javascript')


def about(request):
    return render_to_response('about.html')


def news(request):
    return render_to_response('news.html')


def horses(request):
    return render_to_response('horses.html')


def activity(request, subSite=''):
    return render_to_response('activity.html')
