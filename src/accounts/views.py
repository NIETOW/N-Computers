from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
User = get_user_model()
import re


def signup(request):
    username_taken = False  # Variable pour indiquer si le nom d'utilisateur est déjà pris
    password_valid = True  # Variable pour indiquer si le mot de passe est valide

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Vérifier si le nom d'utilisateur est déjà pris
        if User.objects.filter(username=username).exists():
            username_taken = True
        else:
            # Vérifier les conditions du mot de passe
            if len(password) < 8:
                password_valid = False
            elif not re.search(r"\d", password):
                password_valid = False
            elif not re.search(r"\W", password):
                password_valid = False
            elif not re.search(r"[A-Z]", password):
                password_valid = False

            if password_valid:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('index')

    context = {
        'username_taken': username_taken,
        'password_valid': password_valid
    }
    return render(request, 'accounts/signup.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')
