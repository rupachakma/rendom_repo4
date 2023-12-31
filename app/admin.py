
from django.contrib import admin

from app.models import Category, CustomUser, JobPost, Jobseeker_Profile, Recruiter_Profile, Skills

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Skills)
admin.site.register(Recruiter_Profile)
admin.site.register(Jobseeker_Profile)
admin.site.register(Category)
admin.site.register(JobPost)