
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.cred_index),
    url('change_password/', views.cred_change_password,name="change_password"),
    url('edit_profile/', views.cred_profile,name="edit_profile"),
    url('logout/', views.cred_logout,name="logout"),
]