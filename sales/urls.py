from django.contrib.auth.decorators import login_required
from django.urls import path,include
from django.urls import re_path
from django.contrib.auth import views as auth_views

from .views import index, page_not_found404, SaleCreateView, SaleListView, SaleEditView, SaleDeleteView
from clients.views import registrarCliente2
urlpatterns = [
       
    path('',index, name='inicio'),
    path('not_found/', page_not_found404, name='not_found'),
    path('Venta/add/', login_required(SaleCreateView.as_view()), name='venta_create'),
    path('sale/list/', login_required(SaleListView.as_view()), name='venta_list'),
    path('sale/edit/<int:pk>/',login_required(SaleEditView.as_view()), name='venta_editar'),
    path('sale/eliminar/<int:pk>/',login_required(SaleDeleteView.as_view()), name='venta_eliminar'),
    path('registrarCliente/',login_required(registrarCliente2.as_view()), name='registrarCliente2'),
]