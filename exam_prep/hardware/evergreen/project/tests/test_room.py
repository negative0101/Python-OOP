from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room


class TestRoom(TestCase):
    def setUp(self):
        self.r = Room('A', 100, 2)

    def test_init(self):
        r = Room('A', 100, 2)
        self.assertEqual('A', r.family_name)
        self.assertEqual(100, r.budget)
        self.assertEqual(2, r.members_count)
        self.assertEqual([], r.children)
        self.assertEqual(0, r.expenses)

    def test_expenses_error(self):
        with self.assertRaises(Exception) as ex:
            self.r.expenses = -1
        self.assertEqual('Expenses cannot be negative', str(ex.exception))

    def test_expenses(self):
        self.r.expenses = 10
        self.assertEqual(10, self.r.expenses)

    def test_calculate(self):
        self.assertEqual(0,self.r.expenses)
        c1 = Child(5,4,1)  # 10 * 30
        expected = 300
        self.r.calculate_expenses([c1])
        self.assertEqual(expected, self.r.expenses)
if __name__ == '__main__':
    main()