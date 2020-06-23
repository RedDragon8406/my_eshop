from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login,get_user_model,authenticate
# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')
    context = {
        'login_form':login_form,

    }
    return render(request,'accounts/login.html',context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        new_user = User.objects.create_user(username=user_name, email=email, password=password)
        login(request,new_user)
        return redirect('/')

    context = {
        'register_form': register_form
    }
    return render(request,'accounts/register.html',context)