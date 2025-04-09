# type: ignore
from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import LoginForm, SignupForm
from .models import User


def login_view(
    request,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("question_list")  # Redirect to your home page
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                User.objects.create_user(email=email, password=password)
                messages.success(
                    request, "Account created successfully! Please log in."
                )
                return redirect("login")
            except Exception as e:
                messages.error(request, f"Error creating account: {e}")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def logout_view(request):
    auth_logout(request)
    return redirect("login")
