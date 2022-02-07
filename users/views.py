from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView, DetailView, UpdateView
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from . import models

from . import forms


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("lists:home")
    initial = {"email": "wltn5055@naver.com"}

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("lists:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("lists:home")
    initial = {
        "first_name": "jisu",
        "last_name": "pakr",
        "email": "wltn5055@naver.com",
    }

    def form_valid(self, form):  # form에 user을 저장x
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
