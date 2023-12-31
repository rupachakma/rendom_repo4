from django.urls import path

from app import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('profile/', views.profile_page, name="profile"),
    path('recruiter_update/', views.recruiter_profile_update, name="recruiter_update"),
    path('recruiter_profile_view/', views.recruiter_profile_view, name="recruiter_profile_view"),
    path('jobseeker_update/', views.jobseeker_profile_update, name="jobseeker_update"),
    path('recruiter_profile_view/', views.recruiter_profile_view, name="recruiter_profile_view"),
]
