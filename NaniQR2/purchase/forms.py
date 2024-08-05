from django import forms
from .models import Purchase


class PurchaseIndexForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['Agent_Code']

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['Agent_Code', 'Buyer_Full_Name' , 'Buyer_phone', 'Buyer_UserName', 'Product_Discription', 'Quantity', 'Price', 'Discount_Money', 'Store_No', 'purchased']
    