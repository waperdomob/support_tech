from django.contrib.auth.decorators import login_required
from django.urls import path,include
from django.urls import re_path
from django.contrib.auth import views as auth_views

from .views import  QuoteCreateView, QuoteListView, QuoteEditView, QuoteDeleteView

urlpatterns = [
       
    path('cotizacion/add/', login_required(QuoteCreateView.as_view()), name='cotizacion_create'),
    path('cotizacion/list/', login_required(QuoteListView.as_view()), name='cotizacion_list'),
    path('cotizacion/edit/<int:pk>/',login_required(QuoteEditView.as_view()), name='cotizacion_editar'),
    path('cotizacion/eliminar/<int:pk>/',login_required(QuoteDeleteView.as_view()), name='cotizacion_eliminar'),

]