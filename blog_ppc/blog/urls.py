from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]