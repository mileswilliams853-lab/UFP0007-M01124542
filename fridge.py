from appliance import Appliance

class Fridge(Appliance):
    # Child class for refridgerators
    def __init__(self, name, power_watts, hours_used, cost_per_kwh, compressor_factor=0.4):

        # Call the parent constructor
        super().__init__(name, power_watts, hours_used, cost_per_kwh)

        # Private attribute
        self.__compressor_factor = 0.4

        # Validate compressor factor
        self.set_compressor_factor(compressor_factor)

    # Override the parent's energy calculation
    def calculate_energy_kwh(self):
        normal_energy = super().calculate_energy_kwh()

        # A fridge compressor does not run continuously
        return normal_energy * self.__compressor_factor
