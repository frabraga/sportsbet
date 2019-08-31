from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):

    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def register(request):
    # Get form values
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    messages.success(request, 'You are now register and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')
