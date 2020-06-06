from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields=['title', 'content', 'author', 'img', 'food_type']

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields=['title', 'content', 'img',]