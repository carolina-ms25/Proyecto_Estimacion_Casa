# 🏠 Predictor de Precios de Casas - La Molina

Una aplicación web inteligente que utiliza **Machine Learning** para predecir precios de propiedades en La Molina, Lima, Perú.

![Django](https://img.shields.io/badge/Django-5.1.1-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-purple)

## 🚀 Características

- **Predicción en tiempo real** usando regresión lineal
- **Interfaz moderna** con Bootstrap 5 y Font Awesome
- **Análisis de dataset** con estadísticas visuales
- **Diseño responsivo** para todos los dispositivos
- **Navegación intuitiva** con múltiples páginas

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.1.1
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Base de datos**: SQLite (incluida)
- **Iconos**: Font Awesome 6

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

## 🏃‍♂️ Instrucciones de Instalación y Ejecución

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el Repositorio
```bash
git clone [URL_DEL_REPOSITORIO]
cd AIDeveloper-main
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install django pandas scikit-learn numpy
```

### 4. Ejecutar Migraciones (si es necesario)
```bash
python manage.py migrate
```

### 5. Ejecutar el Servidor de Desarrollo
```bash
python manage.py runserver
```

### 6. Acceder a la Aplicación
Abre tu navegador y ve a: `http://127.0.0.1:8000/`

## 🌐 Opciones de Hosting para Demo

### 1. **Railway** (Recomendado - Gratis)
```bash
# 1. Crear cuenta en railway.app
# 2. Conectar tu repositorio de GitHub
# 3. Railway detectará automáticamente Django
# 4. La app se desplegará automáticamente
```

### 2. **Render** (Gratis)
```bash
# 1. Crear cuenta en render.com
# 2. Conectar repositorio
# 3. Seleccionar "Web Service"
# 4. Configurar comando: python manage.py runserver 0.0.0.0:$PORT
```

### 3. **PythonAnywhere** (Gratis con limitaciones)
```bash
# 1. Crear cuenta gratuita en pythonanywhere.com
# 2. Subir archivos via Files o Git
# 3. Configurar Web App con Django
# 4. Configurar archivos estáticos
```

### 4. **Vercel** (Para proyectos estáticos)
Requiere configuración adicional para Django.

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

## 📈 Mejoras Futuras

- [ ] Agregar más algoritmos de ML (Random Forest, XGBoost)
- [ ] Implementar validación cruzada
- [ ] Agregar gráficos interactivos
- [ ] API REST para predicciones
- [ ] Sistema de usuarios y favoritos
- [ ] Mapas interactivos de La Molina
- [ ] Comparación de propiedades

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 📞 Contacto

**Desarrollador**: [Tu Nombre]
**Email**: [tu-email@example.com]
**Proyecto**: [URL del repositorio]

---

⭐ **¡No olvides dar una estrella al proyecto si te gustó!** ⭐
