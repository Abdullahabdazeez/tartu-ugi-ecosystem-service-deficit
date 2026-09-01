# Methodology

## Analytical framework

The study was designed as a spatial planning workflow connecting urban green-infrastructure condition with ecosystem-service capacity, population-based demand, deficit and intervention priority.

### 1. Study area and spatial alignment

The final reporting area covers **38.8872 km²** in Tartu, Estonia. All final analytical products use **EPSG:3301** and a common **10 m** reporting grid.

### 2. Spectral indicators

Sentinel-2 imagery was used to derive NDVI, EVI, NDMI, NDBI, MNDWI, SAVI and BSI. These indicators describe vegetation vigour, moisture, built-up characteristics, water and exposed surface conditions.

### 3. Urban Green Infrastructure classification

Dynamic World land-cover information was combined with spectral condition to classify seven classes:

- Water
- Dense Urban Forest
- Urban Woodland
- Healthy Green Space
- Stressed Green Space
- Built-up
- Bare Surface

### 4. Ecosystem-service capacity

Capacity was represented on a relative **0–100** scale. UGI class characteristics provided the ecological baseline, while vegetation condition was used to retain within-class variation in vegetated areas. Built-up land was not subjected to an additional imperviousness penalty.

### 5. Ecosystem-service demand

Demand was modelled independently from capacity. WorldPop provided the dominant population signal (**85%**) and built context provided a smaller modifier (**15%**). The demand index ranges from 0 to 1.

### 6. Ecosystem-service deficit

Deficit was calculated as:

**Deficit = Demand × (1 − Capacity/100)**

This makes deficit high where demand is strong and local ecological capacity is weak. No direct Built-up or UGI penalty is included in the deficit formula.

### 7. Planning priority

The continuous deficit surface was classified into five city-wide priority levels using quintile thresholds: Very Low, Low, Moderate, High and Very High.

### 8. Sensitivity analysis

Alternative capacity assumptions, demand weights, deficit formulas and priority-classification schemes were evaluated. The main spatial rankings and hotspot patterns remained stable under reasonable alternative specifications.
