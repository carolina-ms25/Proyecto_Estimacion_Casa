# Predictor de Precios de Casas - La Molina

Una aplicación web inteligente que utiliza **Machine Learning** para predecir precios de propiedades en La Molina, Lima, Perú.

![Django](https://img.shields.io/badge/Django-5.1.1-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-purple)

## Características

- **Predicción en tiempo real** usando regresión lineal
- **Interfaz moderna** con Bootstrap 5 y Font Awesome
- **Análisis de dataset** con estadísticas visuales
- **Diseño responsivo** para todos los dispositivos
- **Navegación intuitiva** con múltiples páginas

## Tecnologías Utilizadas

- **Backend**: Django 5.1.1
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Base de datos**: SQLite (incluida)

## Funcionalidades

### 1. **Página Principal**
- Landing page atractiva con información del proyecto
- Explicación del modelo de ML utilizado
- Navegación clara hacia las funcionalidades

### 2. **Calculadora de Precios**
- Formulario interactivo para ingresar características de la propiedad
- Validación en tiempo real
- Resultados instantáneos con formato profesional

### 3. **Información del Dataset**
- Estadísticas del dataset utilizado
- Rangos de precios y características promedio
- Información técnica del modelo

## URLs de la Aplicación

- **Inicio**: `/` - Página principal con información del proyecto
- **Calculadora**: `/estimar/` - Formulario para estimar precios
- **Dataset**: `/dataset/` - Información y estadísticas del dataset

## Variables del Modelo

El modelo de regresión lineal utiliza las siguientes variables:

1. **Antigüedad** - Años desde la construcción
2. **Número de Pisos** - Niveles de la propiedad  
3. **Dormitorios** - Cantidad de habitaciones
4. **Área Construida** - Metros cuadrados edificados
5. **Área Total** - Metros cuadrados del terreno


## 📊 Funcionalidades

### 1. **Página Principal**
- Landing page atractiva con información del proyecto
- Explicación del modelo de ML utilizado
- Navegación clara hacia las funcionalidades

### 2. **Calculadora de Precios**
- Formulario interactivo para ingresar características de la propiedad
- Validación en tiempo real
- Resultados instantáneos con formato profesional

### 3. **Información del Dataset**
- Estadísticas del dataset utilizado
- Rangos de precios y características promedio
- Información técnica del modelo


## 📱 URLs de la Aplicación

- **Inicio**: `/` - Página principal con información del proyecto
- **Calculadora**: `/estimar/` - Formulario para estimar precios
- **Dataset**: `/dataset/` - Información y estadísticas del dataset
- **Admin**: `/admin/` - Panel de administración de Django

## 🔧 Estructura del Proyecto

```
AIDeveloper-main/
├── data/
│   └── Dataset_La_Molina_cleaned.csv    # Dataset de entrenamiento
├── estimacion_precio_casa/              # Configuración principal
│   ├── settings.py                      # Configuraciones
│   ├── urls.py                         # URLs principales
│   └── ...
├── precio_casa/                        # Aplicación principal
│   ├── templates/                      # Templates HTML
│   │   └── precio_casa/
│   │       ├── home.html              # Página principal
│   │       ├── estimar_precio_casa.html # Calculadora
│   │       └── dataset_info.html       # Info del dataset
│   ├── views.py                       # Lógica de vistas
│   ├── forms.py                       # Formularios
│   ├── model_regresion.py             # Modelo de ML
│   └── ...
└── manage.py                          # Comando principal Django
```

## 🎯 Variables del Modelo

El modelo de regresión lineal utiliza las siguientes variables:

1. **Antigüedad** - Años desde la construcción
2. **Número de Pisos** - Niveles de la propiedad  
3. **Dormitorios** - Cantidad de habitaciones
4. **Área Construida** - Metros cuadrados edificados
5. **Área Total** - Metros cuadrados del terreno
