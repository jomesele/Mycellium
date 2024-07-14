'''
from django import forms
from .models import Order



class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_by'].widget.attrs.update({'class': 'form-control',})
        self.fields['name'].widget.attrs.update({'class': 'form-control',})
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['created'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control',})
        self.fields['delivered'].widget.attrs.update({'class': 'form-control',})
        
    class Meta:
        model = Order
        fields = ['order_by', 'name','contact','address', 'delivered']
        '''