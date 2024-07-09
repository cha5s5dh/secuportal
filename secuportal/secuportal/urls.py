from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from board1 import views as board1_views

# 간단한 홈 페이지 뷰 추가
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board1_views.index, name='home'),
    path('board1/', include('board1.urls')),
    path('board2/', include('board2.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # 로그인 관련 URL
]
