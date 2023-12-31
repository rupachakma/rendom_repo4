from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Skills(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.title

class JobPost(models.Model):
    recruiter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    openings = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    skill_set = models.ManyToManyField(Skills)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Recruiter_Profile(models.Model):
    user_profile = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length = 100)
    address = models.TextField()
    profile_image = models.ImageField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.user_profile.username
    
class Jobseeker_Profile(models.Model):
    user_profile = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    profile_image = models.ImageField(upload_to="img", null=True, blank=True)
    resume = models.FileField(upload_to="resume")

    def __str__(self):
        return self.user_profile.username

class JobApplication(models.Model):
    job_seeker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return f"{self.job_seeker.username} - {self.job_post.title}"