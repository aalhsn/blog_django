from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields=['title', 'content', 'author', 'img', 'profile_img']

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields=['title', 'content', 'img', 'profile_img']