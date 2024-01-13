from django.urls import path,include
from . import views

app_name = "admin"

urlpatterns = [
    path("home/",views.AdminDashboardHomeView.as_view(),name="home"),
    path("secuirty-edit/",views.AdminSecurityEditView.as_view(),name="security-edit"),
    path("profile-edit/",views.AdminProfileEditView.as_view(),name="profile-edit"),
]


