from django.shortcuts import render

def product_list(self, request):
    product = self.request.product
    return render(request,
                  'product/list.html',
                  {'product': product})
