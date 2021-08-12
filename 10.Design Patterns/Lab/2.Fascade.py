class Cutter:
    def cutVegetables(self):
        print('Cutting')


class Boiler:
    def boilVegetables(self):
        print('Boiling')


class Cook(object):
    def prepareDish(self):
        self.cutter = Cutter
        self.cutter.cutVegetables(        )
        self.boiler = Boiler()
        self.boiler.boilVegetables()
