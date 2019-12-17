from django.urls import path
from . import views

urlpatterns = [
    path('mobile', views.mobile, name='mobile'),
    ]