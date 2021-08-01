from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Mirena', 'Female', 'REEEEEEE')

    def test_init_create_attributes(self):
        self.assertEqual('Mirena', self.mammal.name)
        self.assertEqual('Female', self.mammal.type)
        self.assertEqual('REEEEEEE', self.mammal.sound)

    def test_check_sound(self):
        self.assertEqual(f"Mirena makes REEEEEEE", f"{self.mammal.name} makes {self.mammal.sound}")

    def test_check_sound_func(self):
        self.assertEqual(f"Mirena makes REEEEEEE", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_get_kingdom_func(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_get_info(self):
        self.assertEqual('Mirena is of type Female', f"{self.mammal.name} is of type {self.mammal.type}")
    def test_get_info_func(self):
        self.assertEqual('Mirena is of type Female',self.mammal.info())

if __name__ == '__main__':
    main()
