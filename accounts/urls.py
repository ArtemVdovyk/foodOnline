from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.my_account),
    path("register_user/", views.register_user, name="register_user"),
    path("register_vendor/", views.register_vendor, name="register_vendor"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("my_account/", views.my_account, name="my_account"),
    path("customer_dashboard/",
         views.customer_dashboard,
         name="customer_dashboard"),
    path("vendor_dashboard/", views.vendor_dashboard, name="vendor_dashboard"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path("forgot_password/", views.forgot_password, name="forgot_password"),
    path("reset_password_validate/<uidb64>/<token>/",
         views.reset_password_validate,
         name="reset_password_validate"),
    path("reset_password/", views.reset_password, name="reset_password"),
    path("vendor/", include("vendor.urls")),
    path("customer/", include("customers.urls")),
]
