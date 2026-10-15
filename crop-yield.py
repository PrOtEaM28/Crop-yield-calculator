
print("Crop Yield Calculator")

harvested_weight = float(input("Enter harvested weight in kg: "))
land_area = float(input("Enter land area in hectares: "))

if harvested_weight < 0:
    print("Error: Harvested weight cannot be negative.")
elif land_area <= 0:
    print("Error: Land area must be greater than zero.")
else:
    yield_per_hectare = harvested_weight / land_area
    print("Crop yield:", round(yield_per_hectare, 2), "kg/ha")
