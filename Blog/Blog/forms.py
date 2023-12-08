from django import forms

from .models import Blog, BlogArticle


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text']
        labels = {'text': ''}


class BlogArticleForm(forms.ModelForm):
    class Meta:
        model = BlogArticle
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
