from django.db import models
from django.contrib.auth.models import User

class PaymentSettings(models.Model):
    username = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    balance = models.FloatField(blank=True, null=True, default=0)
    apitoken = models.CharField(max_length=255, default=None, null=True, blank=True)
    payment_from = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.username)