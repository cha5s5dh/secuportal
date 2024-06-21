# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('function1/', views.function1, name='function1'),
    path('function2/', views.function2, name='function2'),
    path('function3/', views.function3, name='function3'),
    path('function4/', views.function4, name='function4'),
]
