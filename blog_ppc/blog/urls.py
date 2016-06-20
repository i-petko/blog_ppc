from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from .views import IndexView, PostView, PublishedByView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<slug>\d{4})/$', PublishedByView.as_view(), name='published_by'),
    url(r'^(?P<pk>[0-9]+)/$', PostView.as_view(), name='post'),
]