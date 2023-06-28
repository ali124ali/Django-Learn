from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm #, UserCreationForm
from django.urls import reverse
from django.contrib import messages
from accounts.forms import CustomUserCreationForm
# from django.template.loader import render_to_string
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_str
# from django.db.models.query_utils import Q
# from django.core.mail import EmailMessage


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)

            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')

                else:
                    messages.add_message(request, messages.WARNING, 'User Not Found !!!')

        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')


@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login')

        form = CustomUserCreationForm()
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')


@login_required
def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                logout(request)
                # messages.SUCCESS(request, 'Your password has been changed.')
                return redirect('/accounts/login')
            # else:
            #     messages.ERROR(request, 'Operation failed!\nPlease try again.')

        form = PasswordChangeForm(request)
        context = {'form':form}
        return render(request, 'accounts/password_change_form.html', context)
    else:
        
        return redirect('/') 

