from django.urls import path

from app import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('profile/', views.profile_page, name="profile"),
    path('recruiter_update/', views.recruiter_profile_update, name="recruiter_update"),
    path('recruiter/profile/', views.recruiter_profile_view, name="recruiter_profile_view"),
    path('jobseeker_update/', views.jobseeker_profile_update, name="jobseeker_update"),
    path('jobseeker_profile_view/', views.jobseeker_profile_view, name="jobseeker_profile_view"),
    path('create_jobpost/', views.create_jobpost, name="create_jobpost"),
    path('', views.job_list, name="job_list"),
    path('details/<int:id>', views.job_details, name="job_details"),
    path('update/<int:id>', views.job_update, name="job_update"),
    path('delete/<int:id>', views.delete_job, name="delete_job"),
    path('change/password/', views.change_password, name="change_password"),
    path('job/apply/<int:job_id>', views.job_apply, name="job_apply"),
    path('applications/', views.user_applications, name="user_applications"),
]
