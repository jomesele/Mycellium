from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),

]