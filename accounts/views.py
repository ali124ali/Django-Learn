from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.urls import reverse
from django.contrib import messages
from accounts.forms import CustomUserCreationForm

User = get_user_model()


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
                    messages.add_message(request, messages.SUCCESS, 'You Loged In Successfuly')
                    return redirect('/')

                else:
                    messages.add_message(request, messages.WARNING, 'Are You Signed Up?')
            else:
                messages.add_message(request, messages.ERROR, 'This User Is Not Valid !!!')


        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')


@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'You Loged Out')

    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'You Signed Up Successfuly\nPlease Log In')
                return redirect('/accounts/login')
            else:
                messages.add_message(request, messages.ERROR, 'Operation Failed\nTry Again')

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
                messages.add_message(request, messages.SUCCESS, 'You\'re Password Changed Successfuly')

                logout(request)

                return redirect('/accounts/login')
            else:
                messages.add_message(request, messages.ERROR, 'Operation Failed')

        form = PasswordChangeForm(request)
        context = {'form':form}
        return render(request, 'accounts/password_change_form.html', context)
    else:
        
        return redirect('/') 

