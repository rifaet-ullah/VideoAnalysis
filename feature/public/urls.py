from django.urls import path
from . import views

from feature.public.views import *

app_name = "public"

urlpatterns = [
    path("", SignInView.as_view(), name="sign-in"),
    path("sign-out", sign_out, name="sign-out"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("upload", views.upload, name="upload")
]
