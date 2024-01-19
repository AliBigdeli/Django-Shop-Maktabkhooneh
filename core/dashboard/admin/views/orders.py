from django.views.generic import UpdateView,DeleteView,CreateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission

from dashboard.admin.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import FieldError
from order.models import OrderModel,OrderStatusType

class AdminOrderListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    template_name = "dashboard/admin/orders/order-list.html"
    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size',self.paginate_by)

    def get_queryset(self):
        queryset = OrderModel.objects.all()
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(id__icontains=search_q)
        if status := self.request.GET.get("status"):
            queryset = queryset.filter(status=status)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()  
        context["status_types"] = OrderStatusType.choices
        return context
    
class AdminOrderDetailView(LoginRequiredMixin, HasAdminAccessPermission, DetailView):
    template_name = "dashboard/admin/orders/order-detail.html"

    def get_queryset(self):
        return OrderModel.objects.all()
    
class AdminOrderInvoiceView(LoginRequiredMixin, HasAdminAccessPermission, DetailView):
    template_name = "dashboard/admin/orders/order-invoice.html"

    def get_queryset(self):
        return OrderModel.objects.filter(status=OrderStatusType.success.value)
