from django.urls import path,re_path
from . import views

app_name = "order"

urlpatterns = [
    path("checkout/",views.OrderCheckOutView.as_view(),name="checkout"),
    path("completed/",views.OrderCompletedView.as_view(),name="completed"),

]