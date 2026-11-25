class Appliance:
 # Parent class for all household appliances
    def __init__(self, name, power_watts, hours_used, cost_per_kwh):

        # Private attributes
        self.__name = ""
        self.__power_watts = 0
        self.__hours_used = 0
        self.__cost_per_kwh = 0

        # Set values using validation methods
        self.set_name(name)
        self.set_power_watts(power_watts)
        self.set_hours_used(hours_used)
        self.set_cost_per_kwh(cost_per_kwh)

    # Get methods
    def get_name(self):
        return self.__name

    def get_power_watts(self):
        return self.__power_watts

    def get_hours_used(self):
        return self.__hours_used

    def get_cost_per_kwh(self):
        return self.__cost_per_kwh

    #Set methods with validation
    def set_name(self,name):
        if isinstance(name, str) and name.strip() != "":
            self.__name = name
            return True
        return False

    def set_power_watts(self, power):
        if isinstance(power, (int, float)) and not isinstance(power, bool) and power > 0:
            self.__power_watts = power
            return True
        return False

    def set_hours_used(self, hours):
        if isinstance(hours, (int, float)) and not isinstance(hours, bool) and 0 <= hours <= 24:
            self.__hours_used = hours
            return True
        return False

    def set_cost_per_kwh(self, cost):
        if isinstance(cost, (int, float)) and not isinstance(cost, bool) and cost >= 0:
            self.__cost_per_kwh = cost
            return True
        return False

    #  Electricity consumption calculation
    def calculate_energy_kwh(self):
        energy = (self.__power_watts * self.__hours_used) / 1000
        return energy

    # Electricity cost calculation
    def calculate_cost(self):
        return self.calculate_energy_kwh() * self.__cost_per_kwh
    # Convert appliance information into a row for saving information
    def to_row(self):
        return [
            "Appliance",
            self.__name,
            self.__power_watts,
            self.__hours_used,
            self.__cost_per_kwh
        ]