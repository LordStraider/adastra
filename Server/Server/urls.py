from django.conf.urls import patterns, include, url
from dataManager import views
from django.contrib import admin
# from django.views.generic import RedirectView
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', views.index),
    url(r'^menu/$', views.menu),
    url(r'^siteContent/(?P<site>.+)/$', views.siteContent),
    url(r'^fileLoader/(?P<site>.+)/$', views.fileLoader),

    url(r'^Galleri/(?P<subSite>.+)/$', views.album),
    url(r'^upload/$', views.upload_file),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<site>.+)/$', views.index),

)
