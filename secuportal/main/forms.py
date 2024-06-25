from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Post, Category  # Category 모델을 임포트합니다


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
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'attachment']

    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, label="카테고리")
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="제목")
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="작성자")
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="내용")
    attachment = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False, label="파일 첨부")
