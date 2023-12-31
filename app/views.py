from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from app.forms import Jobseeker_Profile_Update, LoginForm, Profile_Update_Form, Recruiter_Profile_Update, SignupForm
from app.models import Jobseeker_Profile, Recruiter_Profile

# Create your views here.
def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
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
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request,"login.html",{"form":form})

def profile_page(request):
    user = request.user
    if user.is_authenticated:
        if user.user_type == 'recruiter':
            templates_name = 'profile.html'
        elif user.user_type == 'jobseeker':
            templates_name = 'profile.html'
        else:
            return HttpResponse('Invalid User')
    else:
        return HttpResponse('User is not Authenticated')
    return render(request,templates_name)

def logout_page(request):
    logout(request)
    return redirect('login')

def recruiter_profile_update(request):
    user = request.user

    recruiter_profile, created = Recruiter_Profile.objects.get_or_create(user_profile=user)

    if request.method == 'POST':
        user_form = Profile_Update_Form(request.POST, instance=user)
        form = Recruiter_Profile_Update(request.POST, request.FILES, instance=recruiter_profile)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return redirect('recruiter_profile_view')
    else:
        user_form = Profile_Update_Form(instance=user)
        form = Recruiter_Profile_Update(instance=recruiter_profile)

    return render(request, 'profile_update.html', {'form': form,'user_form': user_form})


def recruiter_profile_view(request):
    user = request.user

    try:
        user_profile = user.recruiter_profile
    except Recruiter_Profile.DoesNotExist:
        user_profile = None

    context = {
        'user': user,
        'user_profile': user_profile,
    }

    return render(request, 'profile.html', context)

  
def jobseeker_profile_update(request):
    user = request.user

    jobseeker_profile, created = Jobseeker_Profile.objects.get_or_create(user_profile=user)

    if request.method == 'POST':
        user_form = Profile_Update_Form(request.POST, instance=user)
        form = Jobseeker_Profile_Update(request.POST, request.FILES, instance=jobseeker_profile)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return redirect('recruiter_profile_view')
    else:
        user_form = Profile_Update_Form(instance=user)
        form = Jobseeker_Profile_Update(instance=jobseeker_profile)

    return render(request, 'profile_update.html', {'form': form,'user_form': user_form})


def recruiter_profile_view(request):
    user = request.user

    try:
        user_profile = user.jobseeker_profile
    except Jobseeker_Profile.DoesNotExist:
        user_profile = None

    context = {
        'user': user,
        'user_profile': user_profile,
    }

    return render(request, 'profile.html', context)
  