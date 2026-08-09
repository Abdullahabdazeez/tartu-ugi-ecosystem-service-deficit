# Urban Green Infrastructure and Ecosystem Service Deficit Mapping — Tartu, Estonia

## Project overview

This project assessed how urban green infrastructure is distributed across Tartu and where ecosystem-service capacity is least able to meet urban demand. I developed a geospatial planning framework that integrates remote sensing, land-cover information and population data to move from environmental mapping to practical planning priorities.

The final reporting area covers **38.8872 km²** on a common **10 m** grid in **EPSG:3301**.

## Problem statement

Urban green infrastructure can be substantial at the city scale while still being poorly matched to locations of concentrated demand. Without a spatial assessment of both ecological capacity and demand, green-infrastructure investment may not reach the places where it can provide the greatest planning value.

## Objectives

1. Map and quantify the main UGI classes across Tartu.
2. Estimate relative ecosystem-service capacity.
3. Model population-led ecosystem-service demand.
4. Identify ecosystem-service deficit from the capacity-demand relationship.
5. Classify city-wide planning priorities.
6. Translate the results into practical green-infrastructure recommendations.

## Methodology summary

Sentinel-2 spectral indicators were combined with Dynamic World land-cover information to classify Water, Dense Urban Forest, Urban Woodland, Healthy Green Space, Stressed Green Space, Built-up and Bare Surface. Ecosystem-service capacity was estimated on a 0–100 relative scale. Demand was modelled from WorldPop with population carrying 85% of the weight and built context 15%. Deficit was calculated as **Demand × (1 − Capacity/100)** and classified into five planning-priority levels.

## Key findings

- Built-up land: **21.6040 km² (55.56%)**
- Dense Urban Forest: **7.5759 km² (19.48%)**
- Healthy Green Space: **6.2446 km² (16.06%)**
- Urban Woodland: **2.4494 km² (6.30%)**
- Mean ecosystem-service capacity: **41.54/100**
- Mean ecosystem-service demand: **0.5768**
- Mean ecosystem-service deficit: **0.4110**
- Built-up mean deficit: **0.6751**
- **72.30% of built-up land** occurs within High or Very High planning-priority zones.

## Planning conclusion

The results reveal a clear mismatch between ecological capacity and concentrated urban demand. Existing high-capacity forest and woodland should be protected and connected, while high-priority built-up areas should be assessed for targeted interventions such as street trees, pocket parks, courtyard greening, green roofs and walls, permeable surfaces and stormwater-oriented green infrastructure.

## My contribution

I formulated the planning problem, designed and implemented the geospatial workflow, integrated the datasets, developed the capacity-demand-deficit framework, tested model sensitivity, interpreted the spatial results, produced the maps and translated the findings into planning recommendations.

## Tools and skills

GIS, remote sensing, Sentinel-2, Dynamic World, WorldPop, Python, GeoPandas, Rasterio, NumPy, Pandas, Matplotlib, raster analysis, spatial modelling, ecosystem-service assessment, spatial statistics and cartographic design.