from . import views
from django.urls import path


urlpatterns = [
    path('ScanBooks', views.ScanBooks, name='ScanBooks'),
    #path('decode', views.decodeAjax,name='decodeAjax'),
    #path('up/', views.upload,name='up'),
]