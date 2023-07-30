from django import forms

from clients.models import Cliente

class ClientesForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'telefono1': 'Telefono 1',
            'telefono2': 'Telefono 2',
            'identificacion': 'Numero de identificación o Nit',
            'correo': 'Correo',

        }
        widgets = {
	        'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),            
            'telefono1':forms.TextInput(attrs={'class':'form-control'}),
            'telefono2':forms.TextInput(attrs={'class':'form-control'}),
            'identificacion':forms.NumberInput(attrs={'class':'form-control'}),
            'correo':forms.TextInput(attrs={'class':'form-control'}),
           
        }