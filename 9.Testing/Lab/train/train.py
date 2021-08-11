class Train:
    TRAIN_FULL = "Train is full"
    PASSENGER_EXISTS = "Passenger {} Exists"
    PASSENGER_NOT_FOUND = "Passenger Not Found"
    PASSENGER_ADD = "Added passenger {}"
    PASSENGER_REMOVED = "Removed {}"
    ZERO_CAPACITY = 0

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.passengers = []

    def add(self, passenger_name: str) -> str:
        if len(self.passengers) == self.capacity:
            raise ValueError(self.TRAIN_FULL)

        if passenger_name in self.passengers:
            raise ValueError(self.PASSENGER_EXISTS.format(passenger_name))

        self.passengers.append(passenger_name)
        return self.PASSENGER_ADD.format(passenger_name)

    def remove(self, passenger_name: str) -> str:
        if passenger_name not in self.passengers:
            raise ValueError(self.PASSENGER_NOT_FOUND.format(passenger_name))

        self.passengers.remove(passenger_name)
        return self.PASSENGER_REMOVED.format(passenger_name)


import unittest


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train('Train', 10)

    def test_init(self):
        self.assertEqual('Train', self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_raise_error_one(self):
        self.train.capacity = 0
        with self.assertRaises(Exception) as ex:
            self.train.add('ivan')
        self.assertEqual('Train is full', str(ex.exception))
        self.assertEqual([], self.train.passengers)

    def test_add_raise_error_two(self):
        self.train.add('Ivan')
        with self.assertRaises(Exception) as ex:
            self.train.add('Ivan')
        self.assertEqual('Passenger Ivan Exists', str(ex.exception))
        self.assertEqual(['Ivan'], self.train.passengers)

    def test_add(self):
        res = self.train.add('Ivan')
        self.assertEqual(['Ivan'], self.train.passengers)
        self.assertEqual('Added passenger Ivan',res)

    def test_remove_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.train.remove('Ivan')
        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual([], self.train.passengers)

    def test_remove(self):
        self.train.add('Ivan')
        res = self.train.remove('Ivan')
        self.assertEqual('Removed Ivan',res)