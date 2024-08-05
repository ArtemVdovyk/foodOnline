from django.shortcuts import render


def customer_profile(request):
    return render(request, "customers/customer_profile.html")
