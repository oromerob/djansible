from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^export$', views.export_json, name='export_json'),
   url(r'^ansible_run$', views.ansible_run, name='ansible_run'),
]
