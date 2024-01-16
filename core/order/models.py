from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class OrderStatusType(models.IntegerChoices):
    pending = 1 , "در انتظار پرداخت"
    processing = 2, "در حال پردازش"
    shipped = 3, "ارسال شده"
    delivered = 4,"تحویل شده"
    canceled = 5,"لغو شده"

class UserAddressModel(models.Model):
    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class CouponModel(models.Model):
    code = models.CharField(max_length=100)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    max_limit_usage = models.PositiveIntegerField(default=10)
    used_by = models.ManyToManyField('accounts.User',related_name = "coupon_users")
    
    expiration_date = models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



# Create your models here.
class OrderModel(models.Model):
    user = models.ForeignKey('accounts.User',on_delete=models.PROTECT)
    
    # order address information
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    
    
    total_price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    coupon = models.ForeignKey(CouponModel,on_delete=models.PROTECT,null=True,blank=True)
    status = models.IntegerField(choices=OrderStatusType.choices,default=OrderStatusType.pending.value)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def calculate_total_price(self):
        return sum(item.price * item.quantity for item in self.order_items.all())
    
    def __str__(self):
        return f"{self.user.email} - {self.id}"
    
    
class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel,on_delete=models.CASCADE,related_name="order_items") 
    product = models.ForeignKey('shop.ProductModel',on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.product.title} - {self.order.id}"
    