from django.views.generic import UpdateView,DeleteView,CreateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission

from dashboard.customer.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import FieldError
from order.models import OrderModel

class CustomerOrderListView(LoginRequiredMixin, HasCustomerAccessPermission, ListView):
    template_name = "dashboard/customer/orders/order-list.html"
    paginate_by = 5
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size',self.paginate_by)

    def get_queryset(self):
        queryset = OrderModel.objects.filter(user=self.request.user)
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(id__icontains=search_q)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()    
        return context
    
class CustomerOrderDetailView(LoginRequiredMixin, HasCustomerAccessPermission, DetailView):
    template_name = "dashboard/customer/orders/order-detail.html"

    def get_queryset(self):
        return OrderModel.objects.filter(user=self.request.user)
    
class CustomerOrderInvoiceView(LoginRequiredMixin, HasCustomerAccessPermission, DetailView):
    template_name = "dashboard/customer/orders/order-invoice.html"

    def get_queryset(self):
        return OrderModel.objects.filter(user=self.request.user)
