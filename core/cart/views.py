from typing import Any
from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import JsonResponse
from .cart import CartSession

# Create your views here.
class SessionAddProductView(View):
    
    def post(self,request,*args,**kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        if product_id:
            cart.add_product(product_id)
        return JsonResponse({"cart":cart.get_cart_dict(),"total_quantity":cart.get_total_quantity()})
# Create your views here.
class SessionRemoveProductView(View):
    
    def post(self,request,*args,**kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        if product_id:
            cart.remove_product(product_id)
        return JsonResponse({"cart":cart.get_cart_dict(),"total_quantity":cart.get_total_quantity()})
    
class SessionUpdateProductQuantityView(View):
    
    def post(self,request,*args,**kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        if product_id and quantity:
            cart.update_product_quantity(product_id,quantity)
        return JsonResponse({"cart":cart.get_cart_dict(),"total_quantity":cart.get_total_quantity()})

class SessionCartSummaryView(TemplateView):
    template_name = "cart/cart-summary.html"
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        cart = CartSession(self.request.session)
        cart_items = cart.get_cart_items()
        context["cart_items"] = cart_items
        context["total_quantity"] = cart.get_total_quantity()
        context["total_payment_price"] = cart.get_total_payment_amount()
        return context