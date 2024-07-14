from django import forms

'''
Agent = [Name, Phone, Password]
Customer = [name, phone number, product name, price, store_location]

'''

class PurchaseForm(forms.Form):
    cus_name = forms.CharField(max_length=100)
    product = forms.CharField(max_length=100)
    price = forms.NumberInput(max_length=10)
    message = forms.CharField(widget=forms.Textarea)
    location = forms.EmailField()
    purchased = forms.BooleanField(required=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed']
