from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.forms import BaseForm
from django.http.response import HttpResponse
from django.views.generic import (
    View,
    TemplateView,
    UpdateView,
    ListView,
    DeleteView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.admin.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from accounts.models import Profile
from django.shortcuts import redirect
from django.contrib import messages
from order.models import CouponModel
from django.core.exceptions import FieldError


class AdminCouponListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    template_name = "dashboard/admin/coupons/coupon-list.html"
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = CouponModel.objects.all()
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(code__icontains=search_q)
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


class AdminCouponCreateView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/admin/coupons/coupon-create.html"
    queryset = CouponModel.objects.all()
    form_class = CouponForm
    success_message = "ایجاد تخفیف با موفقیت انجام شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:admin:coupon-edit", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:coupon-list")


class AdminCouponEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/coupons/coupon-edit.html"
    queryset = CouponModel.objects.all()
    form_class = CouponForm
    success_message = "ویرایش تخفیف با موفقیت انجام شد"

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:coupon-edit", kwargs={"pk": self.get_object().pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AdminCouponDeleteView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/admin/coupons/coupon-delete.html"
    queryset = CouponModel.objects.all()
    success_url = reverse_lazy("dashboard:admin:coupon-list")
    success_message = "حذف تخفیف با موفقیت انجام شد"

