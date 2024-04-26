from django.urls import path,include
from .views import dashboard, register

urlpatterns=[
    path("oauth/",include("social_django.urls")),
    path("dashboard/",dashboard,name="dashboard"),
    path("accounts/",include("django.contrib.auth.urls")),
    path("register/",register,name="register")
]