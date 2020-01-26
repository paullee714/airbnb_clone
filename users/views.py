from django.shortcuts import render, redirect, reverse
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class LoginView(View):
    def get(self, request):
        # form = forms.LoginForm()
        form = forms.LoginForm(initial={"email": "test@gmail.com"},)  # initialize form
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
            # print(form.cleaned_data)
            # print(form.is_valid())
            # print(form)
        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


#  function based login view
# def login_view(request):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         pass
