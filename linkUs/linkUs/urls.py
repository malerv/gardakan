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
    url(r'^admin/', include(admin.site.urls)),
)