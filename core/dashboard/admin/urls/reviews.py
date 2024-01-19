from django.urls import path,include
from .. import views

urlpatterns = [
    path("review/list/",views.AdminReviewListView.as_view(),name="review-list"),
    path("review/<int:pk>/edit/",views.AdminReviewEditView.as_view(),name="review-edit"),    
]

