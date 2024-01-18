from django.urls import path,include
from .. import views

urlpatterns = [
    path("wishlist/list/",views.CustomerWishlistListView.as_view(),name="wishlist-list"),
    path("wishlist/<int:pk>/delete/",views.CustomerWishlistDeleteView.as_view(),name="wishlist-delete"),
]

