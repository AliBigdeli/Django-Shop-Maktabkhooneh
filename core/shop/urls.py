from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("product/grid/",views.ShopProductGridView.as_view(),name="product-grid"),
    path("product/<slug:slug>/detail/",views.ShopProductDetailView.as_view(),name="product-detail"),
]

