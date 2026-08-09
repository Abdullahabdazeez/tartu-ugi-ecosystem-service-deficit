# Urban Green Infrastructure and Ecosystem Service Deficit Mapping in Tartu, Estonia

## Executive Summary

Urban green infrastructure plays an important role in making cities healthier, more resilient and more liveable. This study assessed the spatial relationship between urban green infrastructure, ecosystem-service capacity, population-based demand and ecosystem-service deficit across Tartu, Estonia, and translated the results into planning-priority zones.

I developed a geospatial planning framework that combines satellite-derived land-cover and vegetation information with population data. Urban green infrastructure was classified into seven classes: Water, Dense Urban Forest, Urban Woodland, Healthy Green Space, Stressed Green Space, Built-up and Bare Surface. Ecosystem-service capacity was estimated from UGI condition, while demand was modelled mainly from population distribution with a smaller built-environment context component. Ecosystem-service deficit was calculated as **Demand × (1 − Capacity/100)**.

The final reporting area covers **38.8872 km²**. Built-up land covers **21.6040 km² (55.56%)**. Dense Urban Forest covers **7.5759 km² (19.48%)**, Healthy Green Space **6.2446 km² (16.06%)**, and Urban Woodland **2.4494 km² (6.30%)**. Mean ecosystem-service capacity is **41.54/100**, mean demand is **0.5768** and mean deficit is **0.4110**. Built-up areas show the strongest imbalance, with mean capacity of **8.00/100**, mean demand of **0.7339** and mean deficit of **0.6751**. About **72.30% of built-up land** falls within High or Very High planning-priority zones.

## Introduction

Urban forests, woodlands, parks, water bodies and other vegetated spaces support cooling, stormwater regulation, biodiversity, recreation and general environmental quality. For planning purposes, however, the amount of green space alone is not enough. It is also necessary to understand whether ecological capacity is located where urban demand is greatest.

The aim of this study was to assess the distribution and condition of urban green infrastructure in Tartu and identify areas where ecosystem-service provision is least able to meet demand. I approached the project as a geospatial planning problem, using remote sensing, land-cover information and population data to move from environmental mapping to a practical spatial decision-support framework.

## Methodology

Sentinel-2 imagery was used to derive NDVI, EVI, NDMI, NDBI, MNDWI, SAVI and BSI. These indicators were combined with Dynamic World land-cover information to classify the seven UGI and land-cover classes.

Ecosystem-service capacity was estimated on a relative 0–100 scale using UGI class characteristics and continuous vegetation condition. Demand was modelled independently from capacity using WorldPop as the dominant population signal (85%) and built context as a smaller modifier (15%).

Deficit was calculated as **Demand × (1 − Capacity/100)** so that high deficit occurs where demand is high and local ecological capacity is low. The continuous deficit surface was then ranked into Very Low, Low, Moderate, High and Very High planning-priority classes using quintiles.

Sensitivity testing was used to assess whether the main spatial results depended heavily on individual modelling choices. Alternative capacity assumptions, demand weights, deficit formulations and priority-classification schemes produced strongly similar spatial rankings and hotspot patterns.

## Results

Built-up land is the largest class at **55.56%** of the reporting area. Dense Urban Forest accounts for **19.48%**, Healthy Green Space **16.06%**, Urban Woodland **6.30%**, Water **2.16%**, Stressed Green Space **0.42%** and Bare Surface **0.02%**.

Mean ecosystem-service capacity across Tartu is **41.54/100**. Dense Urban Forest records the highest mean capacity at **98.82**, followed by Urban Woodland at **77.81** and Healthy Green Space at **70.43**. Built-up land records a mean capacity of **8.00**.

Mean ecosystem-service demand is **0.5768**. Built-up land records the highest class-level mean demand at **0.7339**. Mean ecosystem-service deficit is **0.4110**, with built-up areas recording a mean deficit of **0.6751**.

The strongest planning result is the concentration of High and Very High priority within built-up land. Approximately **72.30% of built-up land** falls within these two classes, compared with only **0.02% of non-built land**. High and Very High priority classes together cover approximately **15.6229 km² (40.17%)** of the reporting area.

## Discussion

The analysis reveals a clear spatial mismatch between ecological capacity and urban demand in Tartu. The city contains substantial areas of forest, woodland and healthy green space, but these ecological assets are not distributed in the same pattern as the strongest demand. Dense Urban Forest and Urban Woodland provide high relative capacity and generally experience low deficit, whereas the built-up fabric concentrates demand in locations where local ecological capacity is weakest.

This distinction is important for planning. A city can contain considerable green infrastructure and still experience local ecosystem-service deficits. The relevant question is not only how much green space exists, but whether high-quality green infrastructure is positioned, connected and accessible in relation to areas of concentrated need.

## Planning Implications and Recommendations

High-priority built-up areas should be assessed for opportunities to introduce additional vegetation and ecosystem-service functions. Suitable interventions include street-tree planting, pocket parks, vegetated courtyards, green roofs, green walls and conversion of underused hard surfaces to planted or permeable areas.

Dense Urban Forest and Urban Woodland should be treated as strategic ecological assets. Planning decisions should minimise unnecessary fragmentation, protect mature vegetation and maintain connections between larger green areas and the surrounding urban fabric.

Where high-demand neighbourhoods are close to existing green assets, stronger pedestrian and green-network connections can extend their functional value. Bioswales, rain gardens, permeable surfaces, tree pits and vegetated drainage corridors can also support stormwater management while increasing local ecological capacity.

The priority map should be used as a strategic screening tool. Site-level planning should additionally consider land ownership, public access, current land use, engineering constraints, cost, community needs and field conditions.

## Limitations

The UGI classification is a planning-oriented representation derived from remote sensing and land-cover products rather than a field-validated habitat inventory. WorldPop is used as a population-based demand proxy rather than household-level census data. Ecosystem-service capacity is a relative index rather than a direct measurement of individual services such as cooling, carbon sequestration or runoff retention. The five priority classes are relative to conditions within Tartu and should be recalibrated before application elsewhere.

## Conclusion

This study demonstrates how geospatial planning can move beyond mapping green space to identify where ecological provision is least able to meet urban demand. The results show that built-up land contains the strongest concentration of ecosystem-service deficit and planning priority, while forest and woodland generally provide high ecological capacity and low deficit.

The planning implication is to combine protection of existing high-capacity ecological assets with targeted enhancement in urban areas where demand is concentrated and local ecological capacity is weak. The resulting spatial framework provides an evidence base for directing more detailed planning, design and field assessment.

## Author Contribution

I formulated the planning problem, designed and implemented the geospatial workflow, integrated the remote-sensing, land-cover and population datasets, developed the capacity-demand-deficit framework, tested model sensitivity, interpreted the spatial results, produced the cartographic outputs and translated the findings into planning recommendations. External datasets and established geospatial methods remain attributable to their original providers and methodological sources.