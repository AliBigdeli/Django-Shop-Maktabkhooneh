from django.urls import path,re_path
from . import views

app_name = "payment"

urlpatterns = [
    path("verify",views.PayemntVerifyView.as_view(),name="verify"),


]