from .models import Tweet
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'photo']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Type your tweet...',
                'class': 'form-control',
                'rows': 3
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }
        

class UserRegistrationForm(UserCreationForm):
    Email = forms.EmailField()
    class Meta:
        model = User
        fields=('username','email', 'password1','password2')