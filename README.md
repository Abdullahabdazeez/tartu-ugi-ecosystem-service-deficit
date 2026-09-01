# Urban Green Infrastructure and Ecosystem-Service Deficit in Tartu, Estonia

<p align="center">
  <img src="assets/project-board/Tartu_Final_Scientific_Project_Board.png" alt="Tartu urban green infrastructure project board" width="100%">
</p>

## What this project asks

Where does demand for urban ecosystem services exceed the local capacity of green infrastructure in Tartu, and which areas deserve the most planning attention?

I combined Sentinel-2 imagery, Dynamic World land cover and WorldPop population data to map urban green infrastructure, estimate ecosystem-service capacity, model demand and then calculate the spatial deficit between the two.

The result is a planning-oriented way to identify places where green infrastructure is relatively weak compared with the pressure around it.

## Main findings

| Indicator | Result |
|---|---:|
| Reporting area | **38.8872 km²** |
| Built-up land | **21.6040 km² (55.56%)** |
| Dense Urban Forest | **7.5759 km² (19.48%)** |
| Healthy Green Space | **6.2446 km² (16.06%)** |
| Urban Woodland | **2.4494 km² (6.30%)** |
| Stressed Green Space | **0.1626 km² (0.42%)** |
| Vegetated UGI classes (sum of the four rows above) | **16.4325 km² (42.26%)** |
| Mean ecosystem-service capacity | **41.54/100** |
| Mean demand | **0.5768** |
| Mean deficit | **0.4110** |
| Built-up land in High/Very High priority | **72.30%** |
| High + Very High priority area | **15.6229 km² (40.17%)** |

The clearest pattern is a mismatch between ecological capacity and urban demand. Forest and woodland generally provide stronger local capacity, while much of the built-up fabric combines low capacity with higher demand.

## Urban green infrastructure

<p align="center">
  <img src="assets/maps/01_Tartu_Final_UGI_2025.png" alt="Urban green infrastructure in Tartu" width="100%">
</p>

I used Sentinel-2 spectral indicators together with Dynamic World to classify seven urban land and green-infrastructure classes.

## Capacity and demand

<p align="center">
  <img src="assets/maps/02_Tartu_Final_Ecosystem_Service_Capacity.png" alt="Ecosystem-service capacity in Tartu" width="100%">
</p>

<p align="center">
  <img src="assets/maps/03_Tartu_Final_Ecosystem_Service_Demand.png" alt="Ecosystem-service demand in Tartu" width="100%">
</p>

Capacity is expressed on a relative 0–100 scale using green-infrastructure class and vegetation condition. Demand is driven mainly by WorldPop population information, with built context used as a smaller modifier.

These are planning indices, not direct measurements of every ecosystem service.

## Where the deficit is highest

<p align="center">
  <img src="assets/maps/04_Tartu_Final_Ecosystem_Service_Deficit.png" alt="Ecosystem-service deficit in Tartu" width="100%">
</p>

The deficit is calculated as **Demand × (1 − Capacity/100)**. This highlights places where demand is comparatively high but local ecological capacity is weak.

## Planning priority

<p align="center">
  <img src="assets/maps/05_Tartu_Final_Planning_Priority.png" alt="Green-infrastructure planning priority in Tartu" width="100%">
</p>

<p align="center">
  <img src="assets/maps/06_Tartu_Final_Planning_Priority_with_UGI_Context.png" alt="Planning priority with green-infrastructure context in Tartu" width="100%">
</p>

High and Very High priority areas cover about **40.17%** of the reporting area. Within built-up land, **72.30%** falls in those two classes.

The priority map is strongly related to the deficit surface (**Spearman ρ = 0.9802**), which is expected because priority is derived from that deficit ranking.

## How I built the analysis

1. Prepared the Tartu boundary and a common 10 m analysis grid.
2. Derived NDVI, EVI, NDMI, NDBI, MNDWI, SAVI and BSI from Sentinel-2 imagery.
3. Combined spectral condition with Dynamic World to classify urban land and UGI types.
4. Estimated ecosystem-service capacity on a relative 0–100 scale.
5. Modelled demand mainly from WorldPop, with built context as a smaller modifier.
6. Calculated the ecosystem-service deficit.
7. Ranked the continuous deficit into five planning-priority classes.
8. Tested whether the broad pattern remained stable under alternative assumptions.
9. Interpreted the result as a strategic planning screen rather than a site-design answer.

## What this means for planning

The result suggests that much of Tartu's built-up fabric could benefit from targeted green-infrastructure improvement. Depending on local conditions, that might include street trees, pocket parks, courtyard greening, green roofs and walls, permeable surfaces or stormwater-oriented green infrastructure.

At the same time, existing high-capacity forest and woodland should be protected from unnecessary fragmentation.

The map does not tell planners exactly which intervention to build at a specific site. That still requires local information on land ownership, public access, cost, utilities, design constraints and community needs.

## Data sources

Sentinel-2 Surface Reflectance · Dynamic World · WorldPop 2020 · Tartu study boundary

More detail: [`docs/DATA_SOURCES.md`](docs/DATA_SOURCES.md).

## Report and outputs

- [Final report — PDF](report/Tartu_UGI_Ecosystem_Service_Deficit_Final_Report.pdf)
- [Final report — DOCX](report/Tartu_UGI_Ecosystem_Service_Deficit_Final_Report.docx)
- [`assets/maps`](assets/maps/) — final maps
- [`assets/charts`](assets/charts/) — analytical charts
- [`data/processed/tables`](data/processed/tables/) — summary tables
- [`docs`](docs/) — methods, results and limitations

## Limitations

The capacity, demand and deficit layers are relative planning indices. WorldPop is used as a demand proxy rather than household-level population data, and the five priority classes are specific to Tartu. They should not be transferred directly to another city without recalibration.

Site-level decisions still need field information and local planning judgement.

## Author

**Abdullah Abdazeez Ayomide**  
Geospatial Planner · GIS & Remote Sensing Analyst · Urban & Environmental Planning Researcher

[GitHub](https://github.com/Abdullahabdazeez) · [LinkedIn](https://ng.linkedin.com/in/abdazeez-abdullah-4b814719a)

## Citation and licence

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). Code and original documentation are released under the MIT License; external datasets retain their original providers' terms.
