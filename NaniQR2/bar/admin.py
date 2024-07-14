'''
from django.contrib import admin
from .models import Order, Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'address', 'description']
    readonly_fields = ['slug']

admin.site.register(Store, StoreAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_by','slug','contact','created','address', 'delivered', 'delivered_on']
    readonly_fields = ['slug','order_by', 'created']

admin.site.register(Order, OrderAdmin)
'''