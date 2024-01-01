from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from app.forms import ChangePasswordForm, JobApplicationForm, Jobseeker_Profile_Update, LoginForm, PostForm, Profile_Update_Form, Recruiter_Profile_Update, SignupForm
from app.models import JobApplication, JobPost, Jobseeker_Profile, Recruiter_Profile, Skills
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
                return redirect('job_list')
    else:
        form = LoginForm()
    return render(request,"login.html",{"form":form})

@login_required
def profile_page(request):
    user = request.user
    if user.is_authenticated:
        if user.user_type == 'recruiter':
            templates_name = 'joblist.html'
        elif user.user_type == 'jobseeker':
            templates_name = 'joblist.html'
        else:
            return HttpResponse('Invalid User')
    else:
        return HttpResponse('User is not Authenticated')
    return render(request,templates_name)

def logout_page(request):
    logout(request)
    return redirect('login')




# Recruiter views

@login_required
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
        form = Recruiter_Profile_Update(instance=recruiter_profile)  # Correct the instance here

    return render(request, 'recruiter/profile_update.html', {'form': form, 'user_form': user_form})


@login_required
def create_jobpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            jobpost = form.save(commit=False)
            jobpost.recruiter = request.user 
            jobpost.save()

            selected_skill_ids = request.POST.getlist('skill_set')

            selected_skills = Skills.objects.filter(id__in=selected_skill_ids)

            jobpost.skill_set.set(selected_skills)

            return redirect("job_list")
    else:
        form = PostForm()

    return render(request, 'recruiter/create_jobpost.html', {'form': form})


@login_required
def job_update(request,id):
    jobpost = get_object_or_404(JobPost, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=jobpost)
        if form.is_valid():
            jobpost = form.save(commit=False)

            selected_skill_ids = request.POST.getlist('skill_set')
            selected_skills = Skills.objects.filter(id__in=selected_skill_ids)
            jobpost.skill_set.set(selected_skills)
            jobpost.save()

            return redirect("job_list")
    else:
        form = PostForm(instance=jobpost)

    return render(request, 'recruiter/update_jobpost.html', {'form': form, 'jobpost': jobpost})


@login_required
def delete_job(request,id):
    jobpost = get_object_or_404(JobPost,id=id)
    jobpost.delete()
    return redirect("job_list")


@login_required
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
    
    return render(request, 'recruiter/profile.html', context)


def view_applicants(request):
    applications = JobApplication.objects.all()
    return render(request, 'recruiter/view_applicants.html', {'applications': applications})


# views for jobseeker and recruiter

@login_required
def job_list(request):
    job = JobPost.objects.all()
    return render(request,"joblist.html",{'job':job})

@login_required
def job_details(request,id):
    job = get_object_or_404(JobPost, id=id)
    return render(request,"jobdetails.html",{'job':job})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to maintain the user's session
            messages.success(request, 'Password change successfully.')
            return render(request, 'change_password.html')
    else:
        form = ChangePasswordForm(request.user)

    return render(request, 'change_password.html', {'form': form})

#jobseeker views 

@login_required 
def jobseeker_profile_update(request):
    user = request.user

    jobseeker_profile, created = Jobseeker_Profile.objects.get_or_create(user_profile=user)

    if request.method == 'POST':
        user_form = Profile_Update_Form(request.POST, instance=user)
        form = Jobseeker_Profile_Update(request.POST, request.FILES, instance=jobseeker_profile)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return redirect('jobseeker_profile_view')
    else:
        user_form = Profile_Update_Form(instance=user)
        form = Jobseeker_Profile_Update(instance=jobseeker_profile)

    return render(request, 'jobseeker/profile_update.html', {'form': form,'user_form': user_form})

@login_required
def jobseeker_profile_view(request):
    user = request.user

    try:
        user_profile = user.jobseeker_profile
    except Jobseeker_Profile.DoesNotExist:
        user_profile = None

    context = {
        'user': user,
        'user_profile': user_profile,
    }

    return render(request, 'jobseeker/profile.html', context)



@login_required
def job_apply(request, job_id):
    job = JobPost.objects.get(pk=job_id)
    application_form = JobApplicationForm()

    if request.method == 'POST':
        application_form = JobApplicationForm(request.POST, request.FILES)
        if application_form.is_valid():
            application = application_form.save(commit=False)
            application.job_seeker = request.user
            application.job_post = job
            application.save()
            messages.success(request,"Successfully Applied")
            return render(request, "jobseeker/applyjob.html")

    return render(request, "jobseeker/applyjob.html", {'job': job, 'application_form': application_form})


@login_required
def user_applications(request):
    user_applications = JobApplication.objects.filter(job_seeker=request.user)
    return render(request, 'jobseeker/appliedjob.html', {'user_applications': user_applications})