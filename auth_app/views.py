from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from auth_app import forms
from auth_app.forms import SignupForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
        return redirect("login")

    else:
        form = SignupForm()
    data = {'form': form}
    return render(request, "signup.html", data)


@login_required
def special_page(request):
    data = {}
    return render(request, "special.html", data)

def login1(request):
    if request.method == "POST":
        form1 = LoginForm(request.POST)
        if form1.is_valid():
            user = authenticate(username=form1.cleaned_data['username'], password=form1.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("secret")

    else:
        form1 = LoginForm()
    data = {'form1': form1}
    return render(request, "login.html", data)


def index(request):
    data = {}
    return render(request, 'index.html', data)

