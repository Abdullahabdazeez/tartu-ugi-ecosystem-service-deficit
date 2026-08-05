from pathlib import Path
import json
import sys
import pandas as pd
import rasterio

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "project.json",
    "LICENSE",
    "CITATION.cff",
    "requirements.txt",
    "assets/project-cover.png",
    "assets/repository-social-preview.png",
    "notebooks/Project_9_Tartu_UGI_Ecosystem_Service_Deficit.ipynb",
    "outputs/maps/05_planning_priority_zones.png",
    "outputs/charts/06_ugi_by_planning_priority_heatmap.png",
    "data/processed/tables/Final_Project_Key_Results.csv",
    "data/processed/rasters/Tartu_Authoritative_Study_Area_Mask.tif",
]

failures = [f"Missing: {item}" for item in required if not (ROOT/item).exists()]

for path in ROOT.rglob("*"):
    if path.is_file() and path.stat().st_size > 24 * 1024 * 1024:
        failures.append(f"Browser-upload limit exceeded: {path.relative_to(ROOT)}")

try:
    meta = json.loads((ROOT/"project.json").read_text(encoding="utf-8"))
    if abs(meta["high_very_high_priority_pct"] - 52.023288) > 1e-6:
        failures.append("Unexpected priority metadata")
except Exception as exc:
    failures.append(f"Invalid metadata: {exc}")

try:
    with rasterio.open(ROOT/"data/processed/rasters/Tartu_Authoritative_Study_Area_Mask.tif") as ds:
        if ds.count < 1:
            failures.append("Invalid study-area mask")
except Exception as exc:
    failures.append(f"Raster validation failed: {exc}")

if failures:
    print("REPOSITORY VALIDATION: FAILED")
    for failure in failures:
        print("-", failure)
    sys.exit(1)

print("REPOSITORY VALIDATION: PASSED")
print("Required files, headline results, notebook and browser-upload limits are valid.")
