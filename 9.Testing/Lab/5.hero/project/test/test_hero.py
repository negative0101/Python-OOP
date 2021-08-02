import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Harry', 100, 200, 300)
        self.enemy = Hero('Ron', 100, 200, 300)
        self.strong_hero= Hero('Strong Harry',1000,200000,3000)
    def test_init(self):
        self.assertEqual(self.hero.username, 'Harry')
        self.assertEqual(self.hero.level, 100)
        self.assertEqual(self.hero.health, 200)
        self.assertEqual(self.hero.damage, 300)

    def test_battle_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_no_health(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_battle_with_no_health_enemy(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as e:
            self.enemy.battle(self.hero)
        self.assertEqual(f"You cannot fight {self.hero.username}. He needs to rest", str(e.exception))

    def test_battle_draw(self):
        res = self.hero.battle(self.enemy)
        self.assertEqual('Draw',res)

    def test_win(self):
        res = self.strong_hero.battle(self.enemy)
        self.assertEqual('You win',res)
        self.assertEqual(self.strong_hero.health, 170005)
        self.assertEqual(self.strong_hero.damage, 3005)
        self.assertEqual(self.strong_hero.level, 1001)
        self.assertEqual(self.enemy.health, -2999800)
        self.assertEqual(self.enemy.damage, 300)
        self.assertEqual(self.enemy.level, 100)

    def test_battle_lose(self):
        res = self.enemy.battle(self.strong_hero)
        self.assertEqual('You lose',res)
        self.assertEqual(self.strong_hero.health, 170005)
        self.assertEqual(self.strong_hero.damage, 3005)
        self.assertEqual(self.strong_hero.level, 1001)
        self.assertEqual(self.enemy.health, -2999800)
        self.assertEqual(self.enemy.damage, 300)
        self.assertEqual(self.enemy.level, 100)


    def test_str(self):
        self.assertEqual('Hero Harry: 100 lvl\nHealth: 200\nDamage: 300\n',str(self.hero))
