
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('working/', views.working),
]