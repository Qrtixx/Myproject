from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'tags', 'image']
        widgets = {'content': forms.Textarea(attrs={'rows': 10})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ваш комментарий'})}


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Электронная почта')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
