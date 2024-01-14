from django.urls import path, include
from .. import views


urlpatterns = [

    path("home/", views.AdminDashboardHomeView.as_view(), name="home"),
]
