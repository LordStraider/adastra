from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^', 'dataManager.views.index'),
    url(r'^polls/$', 'dataManager.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'dataManager.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'dataManager.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'dataManager.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
