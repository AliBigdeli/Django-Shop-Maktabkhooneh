from django.shortcuts import render,get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,

)


from website.models import NewsLetter,ContactModel
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import *
from django.db.models import F,Q
from django.core import exceptions


class ContactListView(LoginRequiredMixin,HasAdminAccessPermission, ListView):
    title = "لیست تماس ها"
    template_name = "dashboard/admin/contacts/contact-list.html"
    paginate_by = 10
    ordering = "-created_date"

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        queryset = ContactModel.objects.all().order_by("-created_date")
        search_query = self.request.GET.get('q', None)
        ordering_query = self.request.GET.get('ordering', None)

        if search_query:
            queryset = queryset.filter(
                 Q(email__icontains=search_query) |
                 Q(subject__icontains=search_query) |
                 Q(content__icontains=search_query) |
                 Q(phone_number__icontains=search_query)
            )
        if ordering_query:
            try:
                queryset = queryset.order_by(ordering_query)
            except exceptions.FieldError:
                pass
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_result"] = self.get_queryset().count()
        return context



class ContactDetailView(LoginRequiredMixin,HasAdminAccessPermission, DetailView):
    title = "جزئیات تماس"
    template_name = "dashboard/admin/contacts/contact-detail.html"
    
    def get_object(self, queryset=None ):
        contact_obj = get_object_or_404(ContactModel,pk=self.kwargs.get("pk"))
        if not contact_obj.is_seen:
            contact_obj.is_seen = True
            contact_obj.save()
        return contact_obj
    