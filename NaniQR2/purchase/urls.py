from django.urls import path
from .views import (home, 
   PurchaseList, 
   PurchaseDetail, 
   PurchaseCreate, 
   PurchaseUpdate,
   PurchaseDelete
)


urlpatterns = [
    path('', home, name='home'),
    path('purchases/',PurchaseList.as_view(),name='purchases'),
    path('purchase/<int:pk>/',PurchaseDetail.as_view(),name='purchase'),
    path('purchase/create/',PurchaseCreate.as_view(),name='purchase-create'),
    path('purchase/update/<int:pk>/',PurchaseUpdate.as_view(),name='purchase-update'),
    path('purchase/delete/<int:pk>/',PurchaseDelete.as_view(),name='purchase-delete'),
]
