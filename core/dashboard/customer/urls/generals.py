from django.urls import path, include
from .. import views


urlpatterns = [

    path("home/", views.CustomerDashboardHomeView.as_view(), name="home"),
]
