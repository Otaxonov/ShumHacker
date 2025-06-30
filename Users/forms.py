from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Blog.models import User, Post
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'poster', 'content']


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'poster', 'content']
