from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("settings/", views.settings, name="settings"),
    path("register/", views.UserRegistrationForm.as_view(), name="register"),
    path("", views.dashboard, name="dashboard"),
    path("", include("django.contrib.auth.urls")),
]
