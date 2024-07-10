from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    subcategory = forms.CharField(max_length=100, required=True, label='분류', widget=forms.TextInput(attrs={'placeholder': '분류를 입력하세요'}))
    original_time = forms.CharField(required=False, label='원본 시간', widget=forms.TextInput(attrs={'placeholder': '해당 게시글의 원본 시간을 입력하세요'}))

    class Meta:
        model = Post
        fields = ['title', 'subcategory', 'content', 'original_time', 'attachment']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요'}),
            'content': CKEditorWidget(attrs={'placeholder': '내용을 입력하세요'}),
        }
        labels = {
            'title': '제목',
            'subcategory': '분류',
            'content': '내용',
            'original_time': '원본 시간',
            'attachment': '첨부파일',
        }
