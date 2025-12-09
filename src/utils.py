# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 21:19:30 2025

@author: camilo valladares
"""
import ee
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd


# Convertir a EE FeatureCollection
def geodf_to_fc(gdf):
    features = []
    for _, row in gdf.iterrows():
        geom = row["geometry"]
        feat = ee.Feature(ee.Geometry.Point(geom.x, geom.y), {"grid_id": row["grid_id"]})
        features.append(feat)
    return ee.FeatureCollection(features)


# Función para extraer emision para un mes específico
def split_gdf(gdf, chunk_size=1000):
    """Divide el GeoDataFrame en partes más pequeñas."""
    for i in range(0, len(gdf), chunk_size):
        yield gdf.iloc[i:i + chunk_size]
 
        
 
    
# Función general para cualquier gas (eficiente)
def extract_monthly_pollutant(
    dataset,
    variable,
    year,
    month,
    gdf_points,
    chunk_size=1000,
    scale=1000
    ):
    start = datetime(year, month, 1)
    end = start + relativedelta(months=1)

    # Cargar colección
    collection = (
        ee.ImageCollection(dataset)
        .filterDate(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
        .select(variable)
    )
    # 🔵 REGLA ESPECIAL: Filtrar valores negativos solo para SO2
    if "SO2" in variable.upper():
        collection = collection.map(lambda img: img.updateMask(img.gte(0)))
    
    # Verificar disponibilidad
    if collection.size().getInfo() == 0:
        print(f"⚠ No hay datos para {dataset} {year}-{month:02d}")
        return []

    # Promedio mensual
    img = collection.mean()

    # Aplicar QA si existe
    # Algunos productos usan qa_value, otros no
    if "qa_value" in img.bandNames().getInfo():
        img = img.updateMask(img.select("qa_value").gt(0.5))

    results_all = []

    # Procesar por partes
    for chunk in split_gdf(gdf_points, chunk_size):
        fc_chunk = geodf_to_fc(chunk)

        extracted = img.reduceRegions(
            collection=fc_chunk,
            reducer=ee.Reducer.mean(),
            scale=scale
        ).getInfo()

        for f in extracted["features"]:
            props = f["properties"]
            results_all.append({
                "grid_id": props["grid_id"],
                variable: props.get("mean", None),
                "year": year,
                "month": month
            })

    return results_all


# Función para procesar un contaminante en todos los meses

def extract_full_timeseries(dataset, variable, points, start_year=2017, end_year=2022):
    print(f"\n🔵 Iniciando extracción: {dataset} ({variable})")

    all_data = []
    current = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)

    while current <= end_date:
        print(f"  → {current.strftime('%Y-%m')}")
        data = extract_monthly_pollutant(
            dataset,
            variable,
            current.year,
            current.month,
            points
        )
        all_data.extend(data)
        current += relativedelta(months=1)

    df = pd.DataFrame(all_data)
    return df
