import unittest

from appliance import Appliance
from fridge import Fridge
from air_conditioner import AirConditioner


class TestHomeEnergyMonitor(unittest.TestCase):

    # Test appliance creation
    def test_create_appliance(self):
        appliance = Appliance("Test Appliance", 100, 5, 10)
        self.assertEqual(appliance.get_name(), "Test Appliance")

    # Test energy calculation
    def test_energy_calculation(self):
        appliance = Appliance("Test", 1000, 2, 10)
        self.assertEqual(appliance.calculate_energy_kwh(), 2)

    # Test electricity cost
    def test_cost_calculation(self):
        appliance = Appliance("Test", 1000, 2, 10)
        self.assertEqual(appliance.calculate_cost(), 20)

    # Test invalid appliance name
    def test_invalid_name(self):
        appliance = Appliance("Test", 100, 5, 10)
        self.assertFalse(appliance.set_name(""))

    # Test negative power
    def test_negative_power(self):
        appliance = Appliance("Test", 100, 5, 10)
        self.assertFalse(appliance.set_power_watts(-100))

    # Test zero power
    def test_zero_power(self):
        appliance = Appliance("Test", 100, 5, 10)
        self.assertFalse(appliance.set_power_watts(0))

    # Test invalid usage hours
    def test_invalid_hours(self):
        appliance = Appliance("Test", 100, 5, 10)
        self.assertFalse(appliance.set_hours_used(25))

    # Test negative electricity cost
    def test_negative_cost(self):
        appliance = Appliance("Test", 100, 5, 10)
        self.assertFalse(appliance.set_cost_per_kwh(-5))

    # Test fridge compressor factor
    def test_invalid_compressor_factor(self):
        fridge = Fridge("Test Fridge", 150, 24, 10, 0.4)
        self.assertFalse(fridge.set_compressor_factor(2))

    # Test air conditioner creation
    def test_air_conditioner(self):
        ac = AirConditioner("Test AC", 1500, 5, 10)
        self.assertEqual(ac.calculate_energy_kwh(), 7.5)


if __name__ == "__main__":
    unittest.main()
