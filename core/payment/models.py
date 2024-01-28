from django.db import models
from django.db.models import JSONField

class PaymentStatusType(models.IntegerChoices):
    pending = 1, "در انتظار"
    success = 2, "پرداخت موفق"
    failed = 3, "پرداخت ناموفق"


# Create your models here.
class PaymentModel(models.Model):
    authority_id = models.CharField(max_length=255)
    ref_id = models.BigIntegerField(null=True,blank=True)
    amount = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    response_json = JSONField(default=dict)
    response_code = models.IntegerField(null=True,blank=True)
    status = models.IntegerField(choices=PaymentStatusType.choices,default=PaymentStatusType.pending.value)
    
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.authority_id