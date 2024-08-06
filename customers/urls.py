from django.urls import path

from . import views
from accounts import views as account_views


urlpatterns = [
    path("", account_views.customer_dashboard, name="customer"),
    path("profile/", views.customer_profile, name="customer_profile"),
    path("my_orders/", views.my_orders, name="customer_my_orders"),
]
