from django.urls import path,include
from . import views

app_name = "customer"

urlpatterns = [
    path("home/",views.CustomerDashboardHomeView.as_view(),name="home"),

]


