from django.contrib.auth.forms import UserCreationForm
from django import forms  
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')  

    class Meta:  
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')  

