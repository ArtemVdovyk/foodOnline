from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from .models import User, UserProfile
from .utils import detect_user
from vendor.forms import VendorForm


def register_user(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("dashboard")
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data["password"]
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # Create the user using create_user method
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.role = user.CUSTOMER
            user.save()
            messages.success(request,
                             "Your account has been registered successfully!")
            return redirect("register_user")
    else:
        form = UserForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/register_user.html", context=context)


def register_vendor(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("dashboard")
    elif request.method == "POST":
        form = UserForm(request.POST)
        vendor_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and vendor_form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.role = user.VENDOR
            user.save()
            vendor = vendor_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(
                request,
                "Your account has been registered successfully! Please wait for the approval!"
            )
            return redirect("register_vendor")
    else:
        form = UserForm()
        vendor_form = VendorForm()

    context = {
        "form": form,
        "vendor_form": vendor_form
    }

    return render(request, "accounts/register_vendor.html", context=context)


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("dashboard")
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("my_account")
        else:
            messages.error(request, "Invalid login credentials")
            return redirect("login")

    return render(request, "accounts/login.html")


def logout(request):
    auth.logout(request)
    messages.info(request, "You are logged out.")
    return redirect("login")


@login_required(login_url="login")
def my_account(request):
    user = request.user
    redirect_url = detect_user(user)
    return redirect(redirect_url)


@login_required(login_url="login")
def customer_dashboard(request):
    return render(request, "accounts/customer_dashboard.html")


@login_required(login_url="login")
def vendor_dashboard(request):
    return render(request, "accounts/vendor_dashboard.html")
