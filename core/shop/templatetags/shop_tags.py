from django import template
from shop.models import ProductStatusType, ProductModel
register = template.Library()


@register.inclusion_tag("includes/latest-products.html")
def show_latest_products():
    latest_products = ProductModel.objects.filter(
        status=ProductStatusType.publish.value).order_by("-created_date")[:8]
    return {"latest_products": latest_products}


@register.inclusion_tag("includes/similar-products.html")
def show_similar_products(product):
    product_categories= product.category.all()
    similar_prodcuts = ProductModel.objects.filter(
        status=ProductStatusType.publish.value,category__in=product_categories).order_by("-created_date")[:4]
    return {"similar_prodcuts": similar_prodcuts}
