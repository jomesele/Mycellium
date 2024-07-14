from django.db import models
from account.models import MyUser

class Purchase(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    cus_name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    message = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.phone


