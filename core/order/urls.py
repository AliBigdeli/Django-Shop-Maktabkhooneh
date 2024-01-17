from django.urls import path,re_path
from . import views

app_name = "order"

urlpatterns = [
    path("validate-coupon/",views.ValidateCouponView.as_view(),name="validate-coupon"),
    path("checkout/",views.OrderCheckOutView.as_view(),name="checkout"),
    path("completed/",views.OrderCompletedView.as_view(),name="completed"),
    path("failed/",views.OrderFailedView.as_view(),name="failed"),

]