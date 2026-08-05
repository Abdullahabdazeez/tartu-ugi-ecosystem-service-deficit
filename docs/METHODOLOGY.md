# Methodology

## 1. Spatial alignment

All final raster datasets were checked for consistent coordinate reference
system, dimensions, resolution, affine transform and geographic extent.

## 2. Authoritative boundary

The compact urban boundary of Tartu was selected and validated using its area,
geometry type and coordinate reference system. The vector boundary was
rasterized onto the common production grid.

## 3. Production masks

Two masking approaches were used:

- individual valid-data masks for map production
- a common cross-dataset mask for comparative statistics

## 4. Urban green-infrastructure classification

Urban surfaces were represented using seven classes:

- Water
- Dense Urban Forest
- Urban Woodland
- Healthy Green Space
- Stressed Green Space
- Built-up
- Bare Surface

## 5. Ecosystem-service indicators

Three continuous surfaces were assessed:

- ecosystem-service capacity
- ecosystem-service demand
- ecosystem-service deficit

The capacity score uses a 0–100 project scale. Demand and deficit use normalized
0–1 indices.

## 6. Planning-priority classification

The final deficit assessment was translated into five categories:

- Very Low
- Low
- Moderate
- High
- Very High

## 7. Statistical analysis

The final workflow calculated:

- pixel counts
- hectares and square kilometres
- percentage coverage
- continuous descriptive statistics
- indicator correlations
- mean deficit by priority class
- UGI–priority cross-classification

## 8. Cartographic production

Each final map includes:

- authoritative study boundary
- transparent NoData display
- scale bar
- north arrow
- coordinate labels
- legend or colour bar
- neatline
- figure number
- caption
- PNG and PDF exports

## 9. Validation

Validation included:

- boundary-area comparison
- mask-area verification
- raster-alignment checks
- class-total checks
- percentage-total checks
- file-existence checks
- output-dimension and DPI checks
- cross-tabulation consistency
- final-report content registration