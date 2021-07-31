from CarManager.car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car(fuel_capacity=100, fuel_consumption=5.6, make='Test', model='TestModel')

    def test_init_creates_all_attributes(self):
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual('Test', self.car.make)
        self.assertEqual('TestModel', self.car.model)

    def test_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -2
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity(self):
        self.car.fuel_capacity = 2
        self.assertEqual(2, self.car.fuel_capacity)

    def test_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -2
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption(self):
        self.car.fuel_capacity = 2
        self.assertEqual(2, self.car.fuel_capacity)

    def test_empty_make(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make(self):
        self.car.make = 'Asdf'
        self.assertEqual('Asdf', self.car.make)

    def test_empty_model(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model(self):
        self.car.model = 'Asdf'
        self.assertEqual('Asdf', self.car.model)

    def test_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -2
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount(self):
        self.car.fuel_amount = 2
        self.assertEqual(2, self.car.fuel_amount)

    def test_refuel_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-2)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_zero_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_fuel_amount_if_more_than_fuel_capacity(self):
        self.car.refuel(101)
        self.assertEqual(100, self.car.fuel_capacity)

    def test_drive_not_enough_fuel(self):
        self.car.refuel(50)
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.car.refuel(56)
        self.car.drive(1000)
        self.fuel_amount = 0


if __name__ == '__main__':
    main()
