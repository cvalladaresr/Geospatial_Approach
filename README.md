# 📘 Análisis de Emisiones mediante Teledetección para el País Vasco
### Trabajo Final del Máster – Versión 0

Este repositorio contiene el código, datos públicos y material asociado al trabajo final de máster cuyo objetivo es **estimar emisiones y producción industrial mediante teledetección y modelos de machine learning**, aplicados al caso del **País Vasco**.

El proyecto incluye:
- Construcción de una grilla territorial (1 km²)
- Integración de emisiones satelitales mensuales
- Procesamiento y depuración de datos
- Modelos de clasificación (detección de presencia de plantas)
- Modelos de regresión (predicción de producción a nivel planta)
- Paper final del proyecto

## Estructura del Repositorio

```
Proyecto-TFM/
│
├── README.md
├── LICENSE                  # (Opcional)
├── .gitignore
│
├── paper/
│   ├── paper.pdf
│   ├── paper.tex / .docx
│   └── figuras/
│
├── notebooks/
│   ├── 0.1_descarga_datos.ipynb
│   ├── 0.2_eda_y_missing.ipynb
│   ├── 0.3_construccion_bd_final.ipynb
│   ├── 1_clasificacion_planta.ipynb
│   └── 2_prediccion_produccion.ipynb
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── private/             # Datos sensibles (excluidos con .gitignore)
│
├── src/
│   ├── utils/
│   └── models/
│
└── results/
    ├── modelos/
    └── figuras/
```

## Objetivo del Proyecto

**Clasificación**: determinar si existe o no una planta industrial en un punto de la grilla del País Vasco utilizando emisiones observadas y otras variables territoriales.

**Predicción**: estimar la producción industrial mensual de una planta a partir de medidas satelitales y datos ambientales.

## Datos

### Datos públicos incluidos
Archivos geoespaciales y series mensuales de emisiones en `data/raw/` (siempre que sean de libre redistribución).

### Datos NO incluidos
Los datos empresariales usados para entrenamiento y validación **no pueden ser publicados**. Mantenerlos localmente en `data/private/` y añadirlos a `.gitignore`.

## Reproducibilidad

1. Clonar el repositorio:
```
git clone https://github.com/<GITHUB_USERNAME>/<REPO_NAME>.git
cd <REPO_NAME>
```

2. Crear entorno (conda):
```
conda env create -f environment.yml
conda activate tfm
```
ó con pip:
```
pip install -r requirements.txt
```

3. Ejecutar notebooks en orden: notebooks/0.1 → ... → notebooks/2

## Licencia
(Seleccionar e incluir, por ejemplo MIT o CC-BY)

## Contacto
Camilo – Economista & Data Scientist
