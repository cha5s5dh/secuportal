from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Post
from ckeditor.widgets import CKEditorWidget

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")
    
    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
        labels = {
            'username': '사용자 이름',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "비밀번호가 일치하지 않습니다.")

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['category', 'title', 'author', 'content']
