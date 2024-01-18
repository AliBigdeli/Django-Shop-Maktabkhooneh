from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from .forms import SubmitReviewForm
from .models import ReviewModel
from django.contrib import messages

class SubmitReviewView(LoginRequiredMixin, CreateView):
    http_method_names = ["post"]
    model = ReviewModel
    form_class = SubmitReviewForm

    def form_valid(self, form):
        # Assuming your form has a 'product_slug' field
        product = form.cleaned_data['product']
        messages.success(self.request,"دیدگاه شما با موفقیت ثبت شد و پس از بررسی نمایش داده خواهد شد")
        return redirect(reverse_lazy('shop:product-detail',kwargs={"slug":product.slug}))
    
    def form_invalid(self, form):
        messages.error(self.request,"خطایی در ثبت دیدگاه اتفاق افتاد")
        return redirect(self.request.META.get('HTTP_REFERER'))

    def get_queryset(self):
        # You can customize the queryset if needed
        return ReviewModel.objects.filter(user=self.request.user)