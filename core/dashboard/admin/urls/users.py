from django.urls import path,include
from .. import views


urlpatterns = [
    path("user/list/", views.UserListView.as_view(), name="user-list"),
    path("user/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path("user/<int:pk>/edit/", views.UserUpdateView.as_view(), name="user-edit"),
]