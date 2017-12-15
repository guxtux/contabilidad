from django import forms
from apps.reciboUNAM.models import Recibo

class ReciboForm(forms.ModelForm):

    class Meta:
        model = Recibo

        fields = [
            'year',
            'quincena',
            'fecha_pago',
            'neto',
            'comentario',
        ]

        labels = {
            'year': 'Año',
            'quincena': 'Quincena',
            'fecha_pago': 'Fecha pago',
            'neto': 'Cantidad',
            'comentario': 'Comentario',
        }

        widgets = {
            'year': forms.TextInput(attrs={'class':'form-control'}),
            'quincena': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_pago': forms.TextInput(attrs={'class':'form-control'}),
            'neto': forms.TextInput(attrs={'class':'form-control'}),
            'comentario': forms.TextInput(attrs={'class':'form-control'}),
        }