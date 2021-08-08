import unittest
from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):

    def test_init(self):
        pf = PaintFactory('Test', 100)
        self.assertEqual('Test', pf.name)
        self.assertEqual(100, pf.capacity)
        self.assertEqual({}, pf.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], pf.valid_ingredients)

    def test_add_ingredient(self):
        pf = PaintFactory('Test', 100)
        pf.add_ingredient('white', 1)
        self.assertEqual({'white': 1}, pf.ingredients)

    def test_add_ingredient_not_enough_space(self):
        pf = PaintFactory('Test', 1)
        pf.add_ingredient('white', 1)
        with self.assertRaises(Exception) as ex:
            pf.add_ingredient('white', 1)

        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_error_type(self):
        pf = PaintFactory('Test', 1)
        with self.assertRaises(Exception) as ex:
            pf.add_ingredient('asdf', 1)
        self.assertEqual(f"Ingredient of type asdf not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient(self):
        pf = PaintFactory('Test', 1)
        pf.add_ingredient('white', 1)
        pf.remove_ingredient('white', 1)
        self.assertEqual({'white': 0}, pf.ingredients)

    def test_remove_ingredient_below_zero(self):
        pf = PaintFactory('Test', 1)
        pf.add_ingredient('white', 1)
        with self.assertRaises(Exception) as ex:
            pf.remove_ingredient('white', 2)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_not_existing(self):
        pf = PaintFactory('Test', 1)
        with self.assertRaises(Exception) as ex:
            pf.remove_ingredient('asdf', 1)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))