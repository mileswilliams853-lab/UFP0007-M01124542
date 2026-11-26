class Appliance:
    """Parent class for all household appliances."""

    def __init__(self, name, power_watts, hours_used, cost_per_kwh):
        self.set_name(name)
        self.set_power_watts(power_watts)
        self.set_hours_used(hours_used)
        self.set_cost_per_kwh(cost_per_kwh)

    # Getters and setters for appliance information

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Appliance name cannot be empty.")
        self.__name = name.strip()

    def get_power_watts(self):
        return self.__power_watts

    def set_power_watts(self, power):
        if isinstance(power, bool) or not isinstance(power, (int, float)):
            raise ValueError("Power must be a number.")
        if power <= 0:
            raise ValueError("Power must be greater than zero.")
        self.__power_watts = float(power)

    def get_hours_used(self):
        return self.__hours_used

    def set_hours_used(self, hours):
        if isinstance(hours, bool) or not isinstance(hours, (int, float)):
            raise ValueError("Hours must be a number.")
        if hours < 0 or hours > 24:
            raise ValueError("Hours must be between 0 and 24.")
        self.__hours_used = float(hours)

    def get_cost_per_kwh(self):
        return self.__cost_per_kwh

    def set_cost_per_kwh(self, cost):
        if isinstance(cost, bool) or not isinstance(cost, (int, float)):
            raise ValueError("Electricity cost must be a number.")
        if cost < 0:
            raise ValueError("Electricity cost cannot be negative.")
        self.__cost_per_kwh = float(cost)

    # Calculate daily energy consumption

    def calculate_energy_kwh(self):
        return (self.__power_watts * self.__hours_used) / 1000

    # Calculate electricity cost

    def calculate_cost(self):
        return self.calculate_energy_kwh() * self.__cost_per_kwh
