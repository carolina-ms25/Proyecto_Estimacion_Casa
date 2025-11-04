from django import forms

class CasaForm(forms.Form):
    antiguedad = forms.IntegerField(
        label='Antigüedad',
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 5'
        })
    )
    nro_pisos = forms.IntegerField(
        label='Número de pisos', 
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 2'
        })
    )    
    dormitorios = forms.IntegerField(
        label='Dormitorios',
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 3'
        })
    )
    area_constr_m2 = forms.IntegerField(
        label='Área construida en m2',
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 120'
        })
    )
    area_total_m2 = forms.IntegerField(
        label='Área total en m2',
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 150'
        })
    )
