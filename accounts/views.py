from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        messages.error(request, 'testing error message')
        return redirect('register')
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def register(request):
    if request.method == 'POST':
        messages.error(request, 'testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')
