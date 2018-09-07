
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.device_index,name="device"),
    url('device_add/', views.device_add,name="device_add"),
    url('device_update/', views.device_update,name="device_update"),
    url('device_delete/', views.device_delete,name="device_delete"),
]