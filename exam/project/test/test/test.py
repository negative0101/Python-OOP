from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop('Mirena')

    def test_init(self):
        pet_shop = PetShop('Ivan')
        self.assertEqual('Ivan', pet_shop.name)
        self.assertEqual({}, pet_shop.food)
        self.assertEqual([], pet_shop.pets)

    def test_add_food_(self):
        self.pet_shop.add_food('Sharo_hrana', 10)
        self.assertEqual({'Sharo_hrana': 10}, self.pet_shop.food)
        res = self.pet_shop.add_food('Sharo_hrana', 10)
        self.assertEqual({'Sharo_hrana': 20}, self.pet_shop.food)
        self.assertEqual("Successfully added 10.00 grams of Sharo_hrana.", res)

    def test_add_food_error(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_food('hrana', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_error2(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_food('hrana', -10)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_pet(self):
        res = self.pet_shop.add_pet('Ivo')
        self.assertEqual(['Ivo'], self.pet_shop.pets)
        self.assertEqual("Successfully added Ivo.", res)

    def test_add_pet_two(self):
        self.pet_shop.pets = ['Mirena']
        res = self.pet_shop.add_pet('Ivo')
        self.assertEqual(['Mirena', 'Ivo'], self.pet_shop.pets)
        self.assertEqual("Successfully added Ivo.", res)

    def test_add_pet_error(self):
        self.pet_shop.add_pet('Ivo')
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('Ivo')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(['Ivo'], self.pet_shop.pets)

    def test_add_pet_error_two(self):
        self.pet_shop.pets = ['Ivo']
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('Ivo')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(['Ivo'], self.pet_shop.pets)

    def test_feed_pet(self):
        self.pet_shop.add_pet('Ivo')
        self.pet_shop.add_food('hrana_za_ivo', 100)
        res = self.pet_shop.feed_pet('hrana_za_ivo', 'Ivo')
        self.assertEqual("Ivo was successfully fed", res)
        self.assertEqual(0, self.pet_shop.food['hrana_za_ivo'])

    def test_feed_pet_no_pet(self):
        self.pet_shop.add_food('i', 100)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('ivo', 'i')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))
        self.assertEqual({'i': 100}, self.pet_shop.food)

    def test_feed_pet_no_food(self):
        self.pet_shop.pets = ['Ivo', 'Mirena']
        self.pet_shop.food = {'hrana_za_i': 100, 'hrana_za_m': 100}
        res = self.pet_shop.feed_pet('sss', 'Ivo')
        self.assertEqual('You do not have sss', res)

    def test_feed_pet_food_below_100(self):
        self.pet_shop.pets = ['Ivo', 'Mirena']
        self.pet_shop.food = {'hrana_za_i': 100, 'hrana_za_m': 60}
        res = self.pet_shop.feed_pet('hrana_za_m', 'Mirena')
        self.assertEqual("Adding food...", res)
        self.assertEqual(1060.00, self.pet_shop.food['hrana_za_m'])

    def test_repr_za_ivol(self):
        name = f'Shop {self.pet_shop.name}:\n' \
               f'Pets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(name, self.pet_shop.__repr__())


if __name__ == '__main__':
    main()
