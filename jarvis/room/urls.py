
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.room_index,name="room"),
    url('room_add/', views.room_add,name="room_add"),
    url('room_update/(\d*)/', views.room_update,name="room_update"),
    url('room_delete/(\d*)/', views.room_delete,name="room_delete"),
]