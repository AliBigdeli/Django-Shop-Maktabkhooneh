from django.urls import path,include
from .. import views

urlpatterns = [


    path("security/edit/",views.AdminSecurityEditView.as_view(),name="security-edit"),
    path("profile/edit/",views.AdminProfileEditView.as_view(),name="profile-edit"),
    path("profile/image/edit/",views.AdminProfileImageEditView.as_view(),name="profile-image-edit"),
]

