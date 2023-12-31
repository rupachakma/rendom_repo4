from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm

from app.models import CustomUser, JobApplication, JobPost, Jobseeker_Profile, Recruiter_Profile

class SignupForm(UserCreationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    user_type = forms.ChoiceField(label='Join as a:', choices=[('', '-------'),('recruiter', 'Recruiter'),('jobseeker', 'Jobseeker')], widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','user_type']
        label = {'email':'Email'}
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = UsernameField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Recruiter_Profile_Update(forms.ModelForm):
    class Meta:
        model = Recruiter_Profile
        fields = ['company_name','address','profile_image']
        labels = {'company_name':'Company Name','address':'Address','profile_image':'Profile Image'}
        widgets = {
            'company_name':forms.Textarea(attrs={'class':'form-control'}), 
            'address':forms.Textarea(attrs={'class':'form-control'}), 
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class Jobseeker_Profile_Update(forms.ModelForm):
    class Meta:
        model = Jobseeker_Profile
        fields = ['skills','profile_image','resume']
        labels = {'skills':'Skills','profile_image':'Profile Image','resume':'Resume'}
        widgets = {
            'skills': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'resume': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class Profile_Update_Form(forms.ModelForm):
    user_type = forms.ChoiceField(
        label='Join as a:',
        choices=[('', '-------'), ('recruiter', 'Recruiter'), ('jobseeker', 'Jobseeker')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'user_type']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'openings', 'category', 'description', 'skill_set']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'openings': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'skill_set': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }

class ChangePasswordForm(PasswordChangeForm):
    new_password1 = forms.CharField(label="New Password",widget=forms.PasswordInput(attrs={'class': 'form-control'})),
    new_password2 = forms.CharField(label="Confirm New Password",widget=forms.PasswordInput(attrs={'class': 'form-control'})),
    old_password = forms.CharField(label="Current Password",widget=forms.PasswordInput(attrs={'class': 'form-control'})),

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume']
