from django.urls import path

from app import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('profile/', views.profile_page, name="profile"),
    path('', views.job_list, name="job_list"),
    path('details/<int:id>', views.job_details, name="job_details"),
    path('change/password/', views.change_password, name="change_password"),
    path('search_results/', views.search_results, name='search_results'),
    # recruiter path
    path('recruiter_update/', views.recruiter_profile_update, name="recruiter_update"),
    path('recruiter/profile/', views.recruiter_profile_view, name="recruiter_profile_view"),
    path('create/jobpost/', views.create_jobpost, name="create_jobpost"),
    path('update/<int:id>', views.job_update, name="job_update"),
    path('delete/<int:id>', views.delete_job, name="delete_job"),
    path('view/application/', views.view_applicants, name="view_applicants"),

    # jobseeker path
    path('jobseeker/update/', views.jobseeker_profile_update, name="jobseeker_update"),
    path('jobseeker/profile/', views.jobseeker_profile_view, name="jobseeker_profile_view"),
    path('job/apply/<int:job_id>', views.job_apply, name="job_apply"),
    path('your/applications/', views.user_applications, name="user_applications"),
   path('delete_application/<int:application_id>/', views.delete_application, name='delete_application'),
   
    
  
    
    
]
