from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from dataManager.models import Poll
from dataManager import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html')),
    url(r'^polls/$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html')),
    url(r'^polls/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html')),
    url(r'^polls/(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'dataManager.views.vote'),
    url(r'^menu/$', 'dataManager.views.menu'),
    url(r'^polls/menu/$', 'dataManager.views.menu'),
    #url(r'^test_results/$', dataManager.views.test_ajax),
	#url(r'^test/$', dataManager.views.test),
    url(r'^admin/', include(admin.site.urls)),
)
