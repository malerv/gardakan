from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from chatUs import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linkUs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index.html$', views.login, name='home'),
    url(r'^createEvent.html$', views.create_event, name='create_event'),
    url(r'^event.html$', views.event, name='event'),
    url(r'^eventList.html$', views.event_list, name='event_list'),
    url(r'^admin/', include(admin.site.urls)),
    url("", include('django_socketio.urls'))
)