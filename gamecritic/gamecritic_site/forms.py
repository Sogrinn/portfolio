from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Genre


class GameForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    release_date = forms.DateField(label='Release date')
    developer = forms.CharField(label='Developer', max_length=255)
    publisher = forms.CharField(label='Publisher', max_length=255)
    game_genre = forms.ModelMultipleChoiceField(label='Genre(s)', queryset=Genre.objects.all())
    description = forms.CharField(label='Description', widget=forms.Textarea)
    image = forms.ImageField()


class LoginForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class ReviewForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)
    rating = forms.IntegerField(label='Score(1-10)', validators=[MinValueValidator(0), MaxValueValidator(10)])
