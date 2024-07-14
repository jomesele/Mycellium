from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Purchase



class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    context_object_name = 'purchases'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchases'] = context['purchases'].filter(user=self.request.user.pk)
        return context
    
class PurchaseDetail(LoginRequiredMixin, DetailView):
    model = Purchase
    context_object_name = 'purchase'
    
    def get_queryset(self):
        base_qs = super(PurchaseDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    


class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    fields = ['phone','cus_name','product', 'price', 'message', 'location','purchased']
    success_url = reverse_lazy('purchase')
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(PurchaseCreate,self).form_valid(form)
        
    
class PurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    fields = ['phone','cus_name','product', 'price', 'message', 'location','purchased']
    success_url = reverse_lazy('purchase')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(PurchaseUpdate,self).form_valid(form)
      
    def get_queryset(self):
        base_qs = super(PurchaseUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    

    

class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    context_object_name = 'purchase'
    success_url = reverse_lazy('purchase')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(PurchaseDelete,self).form_valid(form)
      
    def get_queryset(self):
        base_qs = super(PurchaseDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)

def home(request):
    return render(request,'home.html')
        