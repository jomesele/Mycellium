from django.shortcuts import render
from .models import Purchase
from .models import PurchaseItem
from .forms import PurchaseCreateForm, PurchaseIndexForm
from cart.cart import Cart
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, Purchase
from account.models import Store ,Agent
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class  CodeView(FormView):
    model = Purchase
    form_class = PurchaseIndexForm
    template_name = 'purchase/entercode.html'
    success_url = reverse_lazy('purchase_create')

    def form_valid(self, form):
        msg = "Code Opened"
        data = form.cleaned_data
        try:
            recipient = Agent.objects.get(category1=data['Agent_Code'])
        except Agent.DoesNotExist:
            return render('purchase/404.html')
        messages.success(self.request, msg)
        return super(CodeView, self).form_valid(form)

@login_required
def purchase_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = PurchaseCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            purchase = form.save()
            for item in cart:
                PurchaseItem.objects.create(purchase=purchase,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            msg = f"-- Purchase Created --\n-- %s --\nAgent code used : %s\nBuyer Full_Name : %s\nBuyer Phone : %s\nBuyer UserName : %s\nProduct Discription : %s\nQuantity : %s\nPrice : %s\nDiscount Money : %s\n Store No. : %s\n "  % (Purchase.objects.get(id=purchase.id).created, 
                            data['Agent_Code'], data['Buyer_Full_Name'], data['Buyer_phone'], 
                            data['Buyer_UserName'], data['Product_Discription'], data['Quantity'], 
                            data['Price'], data['Discount_Money'], data['Store_No']
                            )
            messages.success(request, "Successfull")
            try:
                recipient = Agent.objects.get(category1=data['Agent_Code'])
            except Agent.DoesNotExist:
                return render(request,
                          'purchase/404.html')
            Message.objects.create(sender=request.user, recipient=recipient, content=msg)
            return render(request,
                          'purchase/created.html',
                          {'purchase': purchase})
    else:
        form = PurchaseCreateForm()
    return render(request,
                  'purchase/create.html',
                  {'cart': cart, 'form': form})
