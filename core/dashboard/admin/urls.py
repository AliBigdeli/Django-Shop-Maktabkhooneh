from django.urls import path,include
from . import views

app_name = "admin"

urlpatterns = [
    path("home/",views.AdminDashboardHomeView.as_view(),name="home"),
]


