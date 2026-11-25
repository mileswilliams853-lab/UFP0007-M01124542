# Import our child classes
from fridge import Fridge
from air_conditioner import AirConditioner

# Create a fridge object
my_fridge = Fridge(
    "Samsung Fridge",
    150,
    24,
    10,
    0.4
)

# Create an air conditioner object
my_air_conditioner = AirConditioner(
    "LG Air Conditioner",
    1500,
    5,
    10
)

# Display Home Energy Monitor
print("=" * 40)
print("        HOME ENERGY MONITOR")
print("=" * 40)

# Display fridge information
print("\n--- FRIDGE ---")
print("Appliance: Samsung Fridge")
print(f"Energy Consumption: {my_fridge.calculate_energy_kwh():.2f} kWh")
print(f"Electricity Cost: Rs {my_fridge.calculate_cost():.2f}")

# Display air conditioner information
print("\n--- AIR CONDITIONER ---")
print("Appliance: LG Air Conditioner")
print(f"Energy Consumption: {my_air_conditioner.calculate_energy_kwh():.2f} kWh")
print(f"Electricity Cost: Rs {my_air_conditioner.calculate_cost():.2f}")

# Display total energy consumption and cost
total_energy = (
    my_fridge.calculate_energy_kwh()
    + my_air_conditioner.calculate_energy_kwh()
)

total_cost = (
    my_fridge.calculate_cost()
    + my_air_conditioner.calculate_cost()
)

print("\n" + "=" * 40)
print("          TOTAL SUMMARY")
print("=" * 40)
print(f"Total Energy Consumption: {total_energy:.2f} kWh")
print(f"Total Electricity Cost: Rs {total_cost:.2f}")
print("=" * 40)
