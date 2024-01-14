from django.urls import path, include
from .. import views


urlpatterns = [
    path("product/list/",views.AdminProductListView.as_view(),name="product-list"),
    path("product/<int:pk>/edit/",views.AdminProductEditView.as_view(),name="product-edit")
]
