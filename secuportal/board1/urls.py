from django.urls import path
from . import views

urlpatterns = [
    path('', views.board1_index, name='board1_index'),
    path('category/<str:category>/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/<str:category>/', views.create_post, name='create_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
