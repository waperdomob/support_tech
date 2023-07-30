from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,ListView, UpdateView,DeleteView,DetailView

from clients.models import  Cliente
from clients.forms import ClientesForm



# Create your views here.

class registrarCliente(CreateView):
    model = Cliente    
    form_class= ClientesForm
    template_name = 'cliente_Modal.html'
    success_url = reverse_lazy('clientes')

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):        
        context = {}
        context['title'] = 'LISTA DE CLIENTES'
        context['clientes'] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):        
        return render(request,self.template_name,self.get_context_data())

class listaClientes(ListView):
    model = Cliente    
    form_class= ClientesForm
    template_name = 'clientes.html'
    

    def get_queryset(self):
        return self.model.objects.get_queryset().order_by('id')

    def get_context_data(self,*args, **kwargs):        
        context = {}
        context['title'] = 'LISTA DE CLIENTES'
        context['clientes'] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):              
        return render(request,self.template_name,self.get_context_data())

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClientesForm
    template_name = 'cliente_editModal.html'
    success_url = reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] = 'Editar Cliente'
        context['clientes'] = Cliente.objects.all()        
        return context

class deleteCliente(DeleteView):
    model = Cliente
    template_name = 'cliente_eliminarModal.html'

    def post(self, request,pk, *args, **kwargs):        
        object = Cliente.objects.get(id=pk)
        object.delete()
        return redirect('clientes')

class registrarCliente2(CreateView):
    model = Cliente    
    form_class= ClientesForm
    template_name = 'cliente_Modal.html'
    success_url = reverse_lazy('venta_create')

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):        
        context = {}
        context['title'] = 'LISTA DE CLIENTES'
        context['clientes'] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):        
        return render(request,self.template_name,self.get_context_data())