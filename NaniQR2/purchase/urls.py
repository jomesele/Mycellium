from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.purchase_create, name='purchase_create'),
    path('purchase_index/', views.CodeView.as_view(), name='purchase_index'),
]
