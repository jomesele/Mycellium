from django.contrib import admin
from .models import Purchase, PurchaseItem
from account.models import Agent
# Register your models here.

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    raw_id_fields = ['product']

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'Agent_Code', 'message',
                    'location',
                    'created']
    list_filter = ['created']
    inlines = [PurchaseItemInline]
