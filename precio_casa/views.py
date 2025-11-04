from django.shortcuts import render
from .forms import CasaForm
from .model_regresion import predecir_precio_casa
import pandas as pd
import os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'precio_casa/home.html')

def dataset_info(request):
    # Cargar información del dataset
    try:
        file_path = os.path.join(settings.BASE_DIR, 'data', 'Dataset_La_Molina_cleaned.csv')
        data = pd.read_csv(file_path)
        
        context = {
            'total_properties': len(data),
            'avg_price': data['Precio'].mean(),
            'min_price': data['Precio'].min(),
            'max_price': data['Precio'].max(),
            'avg_area_constr': data['Area_constr_m2'].mean(),
            'avg_area_total': data['Area_total_m2'].mean(),
            'avg_dormitorios': data['Dormitorios'].mean(),
            'avg_antiguedad': data['Antiguedad'].mean(),
        }
    except Exception as e:
        context = {
            'error': 'No se pudo cargar la información del dataset',
            'total_properties': 0,
        }
    
    return render(request, 'precio_casa/dataset_info.html', context)

def estimar_precio_casa(request):
    prediccion=None

    if request.method == 'POST':
        form = CasaForm(request.POST)
        if form.is_valid():
            antiguedad = form.cleaned_data['antiguedad']
            nro_pisos = form.cleaned_data['nro_pisos']
            dormitorios = form.cleaned_data['dormitorios']
            area_constr_m2 = form.cleaned_data['area_constr_m2']
            area_total_m2 = form.cleaned_data['area_total_m2']
            prediccion = predecir_precio_casa(antiguedad, nro_pisos, dormitorios, area_constr_m2, area_total_m2)
    else:
        form = CasaForm()
    return render(request, 'precio_casa/estimar_precio_casa.html', {'form': form, 'prediccion': prediccion})

