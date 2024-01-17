from django.db import models
from django.db.models import JSONField
# Create your models here.


class PaymentStatusType(models.IntegerChoices):
    pending = 1, "در انتظار وضعیت"
    successful = 2, "موفق"
    failed = 3, "نا موفق"


class PaymentModel(models.Model):
    order_id = models.BigIntegerField()
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    ref_id = models.BigIntegerField()
    response_code = models.IntegerField()
    response_json = JSONField(default=dict)
    status = models.IntegerField(
        choices=PaymentStatusType.choices, default=PaymentStatusType.pending.value)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.order_id} - {self.payment.id}"