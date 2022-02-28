from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views import View

from feature.public.forms import SignInForm


class SignInView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect("public:dashboard")
        return render(request, "public/sign_in.html")

    @staticmethod
    def post(request):
        form = SignInForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, "Successfully signed in.")
                return redirect(request.GET.get("next", "/dashboard"))
            else:
                messages.warning(request, "User is not authenticated")
        else:
            for _, errors in form.errors.get_json_data().items():
                for error in errors:
                    messages.info(request, error.get("message"))
        return redirect("public:sign-in")


class DashboardView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "public/dashboard.html")


class UploadView(LoginRequiredMixin, View):
    @staticmethod
    def post(request):
        if request.FILES["upload"]:
            upload_file = request.FILES["upload"]
            file_system_storage = FileSystemStorage()
            file = file_system_storage.save(upload_file.name, upload_file)
            file_url = file_system_storage.url(file)
            return render(request, "public/dashboard.html", {"file_url": file_url})
        return redirect("public:dashboard")


def sign_out(request):
    logout(request)
    messages.success(request, "Successfully signed out.")
    return redirect("public:sign-in")
