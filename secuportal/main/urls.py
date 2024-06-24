from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),
    path('create/', views.create_post, name='create_post'),
    path('signup/', views.signup, name='signup'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # 추가된 URL
]
