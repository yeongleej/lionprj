from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import ResgisterForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            # 로그인정보를 입력한 유저가 존재하는지 유효성 검사
            if user is not None:
                login(request, user)
        return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == "POST":
        form = ResgisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('home')
    else:
        form = ResgisterForm()
        return render(request, 'signup.html', {'form':form})
