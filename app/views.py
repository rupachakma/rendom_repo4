from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from app.forms import LoginForm, SignupForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return render("register")
    else:
        form = LoginForm()
    return render(request,"register.html",{"form":form})


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("Successfully logged in")
    else:
        form = LoginForm()
    return render(request,"login.html",{"form":form})