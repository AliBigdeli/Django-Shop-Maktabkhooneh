from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .cart import CartSession

# Create your views here.
class SessionAddProduct(View):
    
    def post(self,request,*args,**kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        if product_id:
            cart.add_product(product_id)
        return JsonResponse({"cart":cart.get_cart_dict()})
    