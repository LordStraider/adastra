from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from dataManager import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'dataManager.views.index'),
    url(r'^menu/$', 'dataManager.views.menu'),
    url(r'^siteContent/(?P<site>.+)/$', 'dataManager.views.siteContent'),
    url(r'^fileLoader/(?P<site>.+)/$', 'dataManager.views.fileLoader'),

    url(r'^Hem/$', 'dataManager.views.index'),
    url(r'^Om/$', 'dataManager.views.index'),
    url(r'^Nyheter/$', 'dataManager.views.index'),
    url(r'^Hastar/$', 'dataManager.views.index'),
    url(r'^Verksamhet/$', 'dataManager.views.index'),
    url(r'^Verksamhet/(?P<subSite>.+)/$', 'dataManager.views.index'),
    url(r'^Galleri/$', 'dataManager.views.index'),

    url(r'^Galleri/(?P<subSite>.+)/$', 'dataManager.views.album'),

    url(r'^admin/', include(admin.site.urls)),
)
