from django.urls import path, include

from . import views
from accounts import views as account_views


urlpatterns = [
    path("", account_views.vendor_dashboard, name="vendor"),
    path("profile/", views.vendor_profile, name="vendor_profile"),
]
