from fridge import Fridge
from air_conditioner import AirConditioner
from storage import save_appliances, load_appliances


# Load previously saved appliances
appliances = load_appliances()

# Create default appliances if no saved data exists
if not appliances:
    appliances = [
        Fridge("Samsung Fridge", 150, 24, 10, 0.4),
        AirConditioner("LG Air Conditioner", 1500, 5, 10)
    ]


# Display Home Energy Monitor
print("=" * 40)
print("        HOME ENERGY MONITOR")
print("=" * 40)

total_energy = 0
total_cost = 0

for appliance in appliances:
    energy = appliance.calculate_energy_kwh()
    cost = appliance.calculate_cost()

    print(f"\n--- {appliance.get_name()} ---")
    print(f"Energy Consumption: {energy:.2f} kWh")
    print(f"Electricity Cost: Rs {cost:.2f}")

    total_energy += energy
    total_cost += cost


# Display total summary
print("\n" + "=" * 40)
print("          TOTAL SUMMARY")
print("=" * 40)
print(f"Total Energy Consumption: {total_energy:.2f} kWh")
print(f"Total Electricity Cost: Rs {total_cost:.2f}")
print("=" * 40)


# Save appliance information
save_appliances(appliances)

print("\nAppliance information saved successfully!")
