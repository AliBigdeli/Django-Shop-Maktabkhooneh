from django.shortcuts import render
from django.views.generic import View
from .models import PaymentModel,PayemntStatusType
from django.urls import reverse_lazy
from django.shortcuts import redirect,get_object_or_404
from .zarinpal_client import ZarinPalSandbox
# Create your views here.
class PayemntVerifyView(View):
    
    def get(self,request,*args,**kwargs):
        authority_id = request.GET.get("Authority")
        status = request.GET.get("Status")
        payment_obj = get_object_or_404(PaymentModel,authority_id=authority_id)
        zarin_pal = ZarinPalSandbox()
        response = zarin_pal.payment_verify(int(payment_obj.amount),payment_obj.authority_id)
        if response["Status"] == 100 or response["Status"] == 101:
            payment_obj.ref_id = response["RefID"]
            payment_obj.response_code = response["Status"]
            payment_obj.status = PayemntStatusType.success.value
            payment_obj.response_json=response
            payment_obj.save()
            return redirect(reverse_lazy("order:completed"))
        else:
            payment_obj.ref_id = response["RefID"]
            payment_obj.response_code = response["Status"]
            payment_obj.status = PayemntStatusType.failed.value
            payment_obj.response_json=response
            payment_obj.save()
            return redirect(reverse_lazy("order:failed"))
            
        
        