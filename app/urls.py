from django.urls import path

from app import views

urlpatterns = [
    path('', views.register, name="register"),
    path('login', views.login_page, name="login"),
]
