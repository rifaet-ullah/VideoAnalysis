from django.urls import path

from feature.public.views import SignInView, DashboardView, sign_out

app_name = "public"

urlpatterns = [
    path("", SignInView.as_view(), name="sign-in"),
    path("sign-out", sign_out, name="sign-out"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
]
