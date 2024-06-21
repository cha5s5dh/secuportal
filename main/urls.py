from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('security-info/', views.security_info, name='security_info'),
    path('security-info/create-post/', views.post_create, name='post_create'),
    path('security-info/<int:post_id>/', views.post_detail, name='post_detail'),
    path('function2/', views.function2, name='function2'),
    path('function3/', views.function3, name='function3'),
    path('function4/', views.function4, name='function4'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('password-reset/', include('django.contrib.auth.urls')),  # 추가
]
