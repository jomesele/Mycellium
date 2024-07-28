from django import forms
from .models import Purchase


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['Agent_Code' , 'message', 'location', 'purchased']
    