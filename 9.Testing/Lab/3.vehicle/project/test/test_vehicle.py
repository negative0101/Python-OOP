from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle_car = Vehicle(100, 100)

    def test_init_creates_all_attributes(self):
        self.assertEqual(100, self.vehicle_car.fuel)
        self.assertEqual(self.vehicle_car.fuel, self.vehicle_car.capacity)
        self.assertEqual(100, self.vehicle_car.horse_power)
        self.assertEqual(1.25, self.vehicle_car.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        self.vehicle_car.drive(50)
        self.assertEqual(37.5, self.vehicle_car.fuel)

    def test_drive_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle_car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_enough_fuel(self):
        self.vehicle_car.drive(50)
        self.vehicle_car.refuel(37.5)
        self.assertEqual(75, self.vehicle_car.fuel)

    def test_refuel_with_too_much_fuel(self):
        self.vehicle_car.drive(80)
        with self.assertRaises(Exception) as ex:
            self.vehicle_car.refuel(101)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_magic_method(self):
        message = f"The vehicle has {self.vehicle_car.horse_power} " \
                  f"horse power with {self.vehicle_car.fuel} fuel left and {self.vehicle_car.fuel_consumption} fuel consumption"
        self.assertEqual(message, str(self.vehicle_car))


if __name__ == '__main__':
    main()
