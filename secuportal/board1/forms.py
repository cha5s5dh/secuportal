from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'original_time', 'attachment']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 80, 'placeholder': '내용을 입력하세요'}),
            'original_time': forms.DateTimeInput(attrs={'placeholder': '해당 게시글의 원본 시간을 입력하세요'}),
        }
        labels = {
            'title': '제목',
            'content': '내용',
            'original_time': '원본 시간',
            'attachment': '첨부파일',
        }
