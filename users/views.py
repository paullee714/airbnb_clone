from django.shortcuts import render
from django.views import View
from . import forms

# Create your views here.
class LoginView(View):
    def get(self, request):
        # form = forms.LoginForm()
        form = forms.LoginForm(initial={"email": "test@gmail.com"},)  # initialize form
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        # print(form.is_valid())
        # print(form)
        return render(request, "users/login.html", {"form": form})


#  function based login view
# def login_view(request):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         pass
