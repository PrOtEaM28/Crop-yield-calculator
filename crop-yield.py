
print("Crop Yield Calculator")

harvested_weight = float(input("Enter harvested weight in kg: "))
land_area = float(input("Enter land area in hectares: "))

yield_per_hectare = harvested_weight / land_area

print("Crop yield:", yield_per_hectare, "kg/ha")
