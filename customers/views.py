from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.forms import UserProfileForm, UserInfoForm
from accounts.models import UserProfile
from orders.models import Order


@login_required(login_url="login")
def customer_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=profile)
        user_form = UserInfoForm(request.POST, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, "Profile updated")
            return redirect("customer_profile")
        else:
            print(profile_form.errors)
            print(user_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)
        user_form = UserInfoForm(instance=request.user)

    context = {
        "profile": profile,
        "profile_form": profile_form,
        "user_form": user_form,
    }
    return render(request, "customers/customer_profile.html", context=context)


@login_required(login_url="login")
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user, is_ordered=True).order_by("-created_at")
    context = {
        "orders": orders,
    }
    return render(request, "customers/my_orders.html", context=context)
