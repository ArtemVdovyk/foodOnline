from django.urls import path, include

from . import views
from accounts import views as account_views


urlpatterns = [
    path("", account_views.vendor_dashboard, name="vendor"),
    path("profile/", views.vendor_profile, name="vendor_profile"),
    path("menu_builder/", views.menu_builder, name="menu_builder"),
    path("menu_builder/category/<int:pk>/", views.fooditems_by_category,
         name="fooditems_by_category"),

    path("menu_builder/category/add/", views.add_category, name="add_category"),
    path("menu_builder/category/edit/<int:pk>/",
         views.edit_category, name="edit_category"),
    path("menu_builder/category/delete/<int:pk>/",
         views.delete_category, name="delete_category"),

    path("menu_builder/food/add/", views.add_food, name="add_food"),
    path("menu_builder/food/edit/<int:pk>/",
         views.edit_food, name="edit_food"),
    path("menu_builder/food/delete/<int:pk>/",
         views.delete_food, name="delete_food"),

    path("opening_hours/", views.opening_hours, name="opening_hours"),
    path("opening_hours/add/", views.add_opening_hours, name="add_opening_hours"),
    path("opening_hours/remove/<int:pk>/",
         views.remove_opening_hours, name="remove_opening_hours"),
    path("order_details/<int:order_number>/",
         views.order_details, name="vendor_order_details"),
    path("my_orders/", views.my_orders, name="vendor_my_orders"),
]
