
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.dash_index,name="dashboard"),
]