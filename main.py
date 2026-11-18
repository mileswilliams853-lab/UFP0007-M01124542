# Import our child classes
from fridge import Fridge
from air_conditioner import AirConditioner

# Create one fridge object
my_fridge = Fridge(
    "Samsung Fridge",
    150,
    24,
    10,
    0.4
)

# Create one air conditioner object
my_air_conditioner = AirConditioner(
    "LG Air Conditioner",
    1500,
    5,
    10
)

# Create a list containing both objects
appliances = [my_fridge, my_air_conditioner]

# Loop through the appliances
for appliance in appliances:

    print("----------------------------")
    print("Appliance:", appliance.get_name())

    print("Power:", appliance.get_power_watts(), "Watts")

    print("Hours used:", appliance.get_hours_used())

    print("Energy used:", round(appliance.calculate_energy_kwh(), 2), "kWh")

    print("Electricity cost: Rs", round(appliance.calculate_cost(), 2))

print("----------------------------")