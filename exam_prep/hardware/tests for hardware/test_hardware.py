from unittest import  TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):
    def test_init(self):
        hw = Hardware('S','S',1,1)
        self.assertEqual('S',hw.name)
        self.assertEqual('S',hw.type)
        self.assertEqual(1,hw.capacity)
        self.assertEqual(1,hw.memory)
        self.assertEqual([],hw.software_components)

    def test_install(self):
        sw = Software('S','S',1,1)
        hw = Hardware('S','S',1,1)
        hw.install(sw)
        self.assertEqual([sw],hw.software_components)

    def test_cannot_install(self):
        hw = Hardware('S','S',1,1)
        sw = Software('S','S',2,2)
        with self.assertRaises(Exception) as ex:
            hw.install(sw)
        self.assertEqual("Software cannot be installed",str(ex.exception))
        self.assertEqual([],hw.software_components)

    def test_uninstall(self):
        sw = Software('S','S',1,1)
        hw = Hardware('S','S',1,1)
        hw.install(sw)
        hw.uninstall(sw)
        self.assertEqual([],hw.software_components)


if __name__ == '__main__':
    main()