from django.urls import path,include
from .. import views

urlpatterns = [
    path("order/list/",views.CustomerOrderListView.as_view(),name="order-list"),
    path("order/<int:pk>/detail/",views.CustomerOrderDetailView.as_view(),name="order-detail"),
    path("order/<int:pk>/invoice/",views.CustomerOrderInvoiceView.as_view(),name="order-invoice"),
]

