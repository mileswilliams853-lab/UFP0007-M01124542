from appliance import Appliance


class Fridge(Appliance):
    # Child class for refrigerators

    def __init__(self, name, power_watts, hours_used, cost_per_kwh, compressor_factor=0.4):

        # Call the parent constructor
        super().__init__(name, power_watts, hours_used, cost_per_kwh)

        # Private attribute
        self.__compressor_factor = 0.4

        # Validate compressor factor
        self.set_compressor_factor(compressor_factor)

    # Getter method
    def get_compressor_factor(self):
        return self.__compressor_factor

    # Setter method with validation
    def set_compressor_factor(self, factor):

        if isinstance(factor, (int, float)) and not isinstance(factor, bool) and 0 < factor <= 1:
            self.__compressor_factor = factor
            return True

        return False

    # Override the parent's energy calculation
    def calculate_energy_kwh(self):

        normal_energy = super().calculate_energy_kwh()

        # A fridge compressor does not run continuously
        return normal_energy * self.__compressor_factor

