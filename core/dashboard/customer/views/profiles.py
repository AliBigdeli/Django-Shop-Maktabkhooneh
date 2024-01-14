from django.http import HttpResponse
from django.views.generic import View, TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.customer.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from accounts.models import Profile
from django.shortcuts import redirect
from django.contrib import messages


class CustomerSecurityEditView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = "dashboard/customer/profile/security-edit.html"
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy("dashboard:customer:security-edit")
    success_message = "بروز رسانی پسورد با موفقیت انجام شد"


class CustomerProfileEditView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/customer/profile/profile-edit.html"
    form_class = CustomerProfileEditForm
    success_url = reverse_lazy("dashboard:customer:profile-edit")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

class CustomerProfileImageEditView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names=["post"]
    model = Profile
    fields= [
        "image"
    ]
    success_url = reverse_lazy("dashboard:customer:profile-edit")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)