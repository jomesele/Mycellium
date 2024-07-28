from django.db import models
from account.models import Store , Agent
from catagories.models import Product

class Purchase(models.Model):
    Agent_Code = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Purchase {}'.format(self.id)
    
class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

class Message(models.Model):
    sender = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='received_messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

