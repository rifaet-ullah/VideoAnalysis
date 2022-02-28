from django.urls import path

from feature.public.views import SignInView, sign_out, DashboardView, UploadView

app_name = "public"

urlpatterns = [
    path("", SignInView.as_view(), name="sign-in"),
    path("sign-out", sign_out, name="sign-out"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("upload", UploadView.as_view(), name="upload"),
]
