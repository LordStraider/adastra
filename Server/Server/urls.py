from django.conf.urls import patterns, include, url
from dataManager import views
from django.contrib import admin
# from django.views.generic import RedirectView
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'', include('social_auth.urls')),
    url(r'^administrationpage/submitMenu/$', views.submitMenu),
    url(r'^administrationpage/submitContent/$', views.submitContent),
    url(r'^administrationpage/menu/$', views.menu),
    url(r'^administrationpage/siteContent/(?P<site>.+)/$', views.siteAdminContent),
    url(r'^administrationpage/fileLoader/(?P<site>.+)/$', views.fileLoader),
    url(r'^administrationpage/upload/$', views.upload_files),
    url(r'^administrationpage/logout/$', views.logout),
    url(r'^administrationpage/(?P<site>.+)/$', views.admin_index),
    url(r'^administrationpage/$', views.admin_index),

    url(r'^$', views.index),
    url(r'^checkLoggedIn/$', views.checkLoggedIn),
    url(r'^menu/$', views.menu),
    url(r'^siteContent/(?P<site>.+)/$', views.siteContent),
    url(r'^fileLoader/(?P<site>.+)/$', views.fileLoader),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<site>.+)/$', views.index),
)
