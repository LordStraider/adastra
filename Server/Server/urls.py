from django.conf.urls import patterns, include, url
from dataManager import views
from django.contrib import admin
# from django.views.generic import RedirectView
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^administrationpage/$', views.admin_index),
    url(r'^administrationpage/menu/$', views.menu),
    url(r'^administrationpage/siteContent/(?P<site>.+)/$', views.siteAdminContent),
    url(r'^administrationpage/fileLoader/(?P<site>.+)/$', views.fileLoader),

    url(r'^administrationpage/upload/$', views.upload_file),

    url(r'^administrationpage/(?P<site>.+)/$', views.admin_index),
)


urlpatterns += patterns(
    '',
    url(r'^$', views.index),
    url(r'^menu/$', views.menu),
    url(r'^siteContent/(?P<site>.+)/$', views.siteContent),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<site>.+)/$', views.index),

)
