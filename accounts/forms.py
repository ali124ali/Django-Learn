# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #, AuthenticationForm
from django import forms  
from django.contrib.auth import get_user_model
# from accounts.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')  

    class Meta:  
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')  

