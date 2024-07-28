from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
    cus_name = forms.CharField(max_length=100)
    price = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)
    location = forms.CharField()
    purchased = forms.BooleanField(required=False)

    
