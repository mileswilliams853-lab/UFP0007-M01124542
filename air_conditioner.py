from appliance import Appliance

class AirConditioner(Appliance):
    # Child class for air conditioners

    def __init__(self, name, power_watts, hours_used, cost_per_kwh):
        # Call the parent constructor
        super().__init__(name, power_watts, hours_used, cost_per_kwh)

    # Override the parent's energy calculation
    def calculate_energy_kwh(self):
        # Air conditioner uses its full rated power
        energy = (self.get_power_watts() * self.get_hours_used()) / 1000

        return energy

     # Convert air conditioner information into a row for saving
    def to_row(self):
        return [
            "AirConditioner",
            self.get_name(),
            self.get_power_watts(),
            self.get_hours_used(),
            self.get_cost_per_kwh()
        ]
