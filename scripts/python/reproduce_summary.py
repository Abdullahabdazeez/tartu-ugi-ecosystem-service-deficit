from pathlib import Path
import math
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
TABLES = ROOT / "data" / "processed" / "tables"

key = pd.read_csv(TABLES / "Final_Project_Key_Results.csv")
values = dict(zip(key["Indicator"], key["Value"]))

checks = {
    "Authoritative compact urban study area": 38.887971,
    "Built-up surface": 55.097821,
    "Vegetated UGI coverage": 42.737456,
    "Tree-based UGI coverage": 25.315014,
    "High and Very High planning priority": 52.023288,
    "Very High planning priority": 31.094293,
    "Built-up land in High or Very High priority zones": 19.9552,
    "Mean ecosystem service capacity": 36.710318,
    "Mean ecosystem service demand": 0.378701,
    "Mean ecosystem service deficit": 0.513534,
}

for metric, expected in checks.items():
    actual = float(values[metric])
    if not math.isclose(actual, expected, rel_tol=0, abs_tol=1e-6):
        raise ValueError(f"{metric}: expected {expected}, found {actual}")

print("RESULT REPRODUCTION: PASSED")
print(f"Study area: {values['Authoritative compact urban study area']:.2f} km²")
print(f"Vegetated UGI coverage: {values['Vegetated UGI coverage']:.2f}%")
print(f"High + Very High priority: {values['High and Very High planning priority']:.2f}%")
print(f"Mean ecosystem-service deficit: {values['Mean ecosystem service deficit']:.4f}")
