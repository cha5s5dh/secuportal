import os
import django

# Django 프로젝트의 설정을 설정합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secuportal.settings')
django.setup()

from main.models import Category

# 보안뉴스 카테고리 추가
news_categories = ['임시1', '임시2', '임시3', '임시4', '임시5']
for name in news_categories:
    Category.objects.get_or_create(name=name, type='news')

print("보안뉴스 카테고리 추가 완료")
