from django.shortcuts import render
from .models import Purchase
from .models import PurchaseItem
from .forms import PurchaseCreateForm
from cart.cart import Cart
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from account.models import Store ,Agent


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
            msg = ' Agent %s code used for purchase in %s Store on %s' % (data['Agent_Code'], request.user.name, Purchase.objects.get(id=purchase.id).created)
            messages.success(request, msg)
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
