from django import forms

from sales.models import *

class cotizacionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'


    class Meta:
        model = Cotizacion
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control select2','style': 'width: 100%'}),
            'fecha': forms.DateInput(format='%Y-%m-%d',attrs={'class': 'form-control','value': datetime.now().strftime('%Y-%m-%d'),'readonly':True}),
            'subtotal': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 100%','readonly': True}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 100%'}),
            'total': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 100%','readonly': True}),

        }