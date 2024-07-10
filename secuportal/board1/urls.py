from django.urls import path
from . import views

urlpatterns = [
    path('', views.board1_index, name='board1_index'),
    path('category/<str:category>/', views.post_list, name='post_list'),
    path('create/<str:category>/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
