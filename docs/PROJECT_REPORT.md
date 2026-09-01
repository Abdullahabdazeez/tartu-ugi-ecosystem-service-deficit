# Project Report: Urban Green Infrastructure and Ecosystem-Service Deficit in Tartu

## Background

A city can have a reasonable amount of green space overall and still have neighbourhoods where ecological capacity is weak compared with local demand.

I developed this project to look for that mismatch in Tartu, Estonia. The aim was not simply to map where green areas exist, but to ask where urban demand is high while nearby green-infrastructure capacity is relatively low.

## What I did

I used Sentinel-2 imagery, Dynamic World land cover and WorldPop population data on a common 10 m grid.

The workflow first classified urban green infrastructure, then estimated ecosystem-service capacity on a relative 0-100 scale. Demand was modelled mainly from population, with built context used as a smaller modifier.

I calculated the deficit as **Demand × (1 - Capacity/100)** and then ranked the continuous deficit surface into five planning-priority classes.

## What I found

Built-up land covers **21.6040 km², or 55.56%** of the reporting area. Vegetated green-infrastructure classes together cover about **16.4325 km², or 42.26%**.

Mean ecosystem-service capacity is **41.54/100**, mean demand is **0.5768**, and mean deficit is **0.4110**.

The most important planning pattern appears inside the built-up fabric. **72.30% of built-up land** falls within the High or Very High planning-priority classes.

Across the whole reporting area, High and Very High priority together cover about **15.6229 km², or 40.17%**.

## What the result means

The model highlights places where local ecological capacity appears weak relative to demand. Those areas may deserve closer attention for interventions such as street trees, pocket parks, courtyard greening, green roofs, permeable surfaces or stormwater-oriented green infrastructure.

The result also supports protecting existing forest and woodland where ecological capacity is already high.

## What the result does not mean

The capacity, demand and deficit layers are relative planning indices. They are not direct measurements of every ecosystem service, and the priority classes are specific to Tartu.

A High-priority pixel does not automatically tell a planner which intervention should be built there. Site design still needs information on ownership, access, infrastructure constraints, cost and community needs.

## Why I used both capacity and demand

A green-space map alone tends to focus on supply. A population map alone tends to focus on pressure. The deficit approach brings the two together.

That is useful because two places with similar amounts of green cover can have very different planning needs if one serves a much larger or denser surrounding population.

## What I would add next

A stronger next version would include walking access to public green spaces, land ownership, heat exposure, stormwater need and neighbourhood-level demographic information.

That would allow the priority map to move from a general ecosystem-service screen toward more specific intervention planning.

## Main outputs

Final maps are in [`assets/maps`](../assets/maps/), charts in [`assets/charts`](../assets/charts/), processed result tables in [`data/processed/tables`](../data/processed/tables/) and the full technical report is in [`report`](../report/).

## Final note

The main value of the project is the shift from asking "where is green space?" to asking "where is green infrastructure most needed relative to local demand?"
