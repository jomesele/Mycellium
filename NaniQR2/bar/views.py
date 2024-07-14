
from django.views.generic import DetailView, CreateView, ListView, FormView
from django.views.decorators.csrf import csrf_exempt
from . import barCode
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
import base64
from  .decode import Decoder
from  .models import Order
from account.models import MyUser
from io import BytesIO
from PIL import Image
import json
#from .forms import OrderForm

@csrf_exempt
def ScanBooks(request):
    if request.method == "POST":
        jsonData = json.loads(request.body)
        metarCode = jsonData.get('Metar', secure = True)
        image = Image.open(BytesIO(metarCode))
        decoder = Decoder()
        result = decoder.decode(image).decode("utf-8")
        if result != '':
            return JsonResponse({
                "method": "decode",
                "success": True,
                "result": result,
                "coordinates": decoder.code_quad
                })
        else:
            return JsonResponse({
                "method": "decode",
                "success": False,
                "error": "no ChromaQR code was found in the uploaded image"
            })
'''
class OrderView(FormView):
    template_name = 'order_form.html'
    form_class = OrderForm
    success_url = 'profile'
    
    def form_valid(self, form):
        form.save()

        return super(OrderView, self).form_valid(form)

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = 'Product_order_conform'

    def get_context_data(self,  object_list=None, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['order_by'] = get_object_or_404(Store, slug=self.kwargs['slug'])
        context['name'] = get_object_or_404(Store.user, slug=self.kwargs['slug'])
        context['address'] = get_object_or_404(Store.address, slug=self.kwargs['slug'])
        context['delivered'] = get_object_or_404(Order.delivered, slug=self.kwargs['slug'])

        return context
    
class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(order_by=self.request.user)
'''