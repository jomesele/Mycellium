from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db import models
from django_extensions.db import fields as extension_fields
from django.utils import timezone
from account.models import MyUser


class Store(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media/Company-logo/", null=True, blank=True)

    def __str__(self):
        return u'%s' % self.slug

class Order(models.Model):
    order_by = models.CharField(max_length=40, null=True, blank=True)
    derscription = models.CharField(max_length=100, null=True, blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    address = models.TextField(blank=True, null=True)
    count = models.IntegerField(default=1)
    cost = models.IntegerField(default=0)
    delivered = models.BooleanField(default=False)
    delivered_on = models.DateTimeField(blank=True, null=True)
    # Relationship Fields
    '''
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE, related_name="orders", null=True, blank=True
    )
    '''
    class Meta:
        ordering = ('delivered','-created',)
        

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Product_order_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Product_order_update', args=(self.slug,))


    def save(self, *args, **kwargs):
        if self.delivered:
            if not self.delivered_on:
                self.delivered_on = timezone.now()
        super(Order, self).save(*args, **kwargs)
