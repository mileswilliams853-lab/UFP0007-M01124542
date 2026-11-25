import csv
import os

from fridge import Fridge
from air_conditioner import AirConditioner

# Save appliance information to a CSV file
def save_appliances(appliances, filename="appliances.csv"):

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # Write column headings
        writer.writerow([
            "Type",
            "Name",
            "Power Watts",
            "Hours Used",
            "Cost Per kWh",
            "Compressor Factor"
        ])

        # Save each appliance
        for appliance in appliances:
            writer.writerow(appliance.to_row())

# Load appliance information from a CSV file
def load_appliances(filename="appliances.csv"):
    appliances = []

    # Check whether the CSV file exists
    if not os.path.exists(filename):
        return appliances
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        # Skip the headings
        next(reader, None)

        # Read each appliance
        for row in reader:
            try:
                appliance_type = row[0]
                name = row[1]
                power = float(row[2])
                hours = float(row[3])
                cost = float(row[4])

                # Recreate a fridge object
                if appliance_type == "Fridge":
                    compressor_factor = float(row[5])
                    appliance = Fridge(
                        name,
                        power,
                        hours,
                        cost,
                        compressor_factor
                    )
                    appliances.append(appliance)

                # Recreate an air conditioner object
                elif appliance_type == "AirConditioner":
                    appliance = AirConditioner(
                        name,
                        power,
                        hours,
                        cost
                    )
                    appliances.append(appliance)
            except (ValueError, IndexError):
                print("Warning: Invalid appliance data found.")
    return appliances
