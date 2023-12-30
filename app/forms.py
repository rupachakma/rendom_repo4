from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

from app.models import CustomUser

class SignupForm(UserCreationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    user_type = forms.ChoiceField(label='Join as a:', choices=[('', '-------'),('recruiter', 'Recruiter'),('jobseeker', 'Jobseeker')], widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username','email','user_type']
        label = {'email':'Email'}
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = UsernameField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))