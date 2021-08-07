from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_list = [f for f in self.supplies if f.__class__.__name__ == 'FoodSupply']
        if food_list:
            return food_list
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        water_list = [w for w in self.supplies if w.__class__.__name__ == 'WaterSupply']
        if water_list:
            return water_list
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        painkiller_list = [p for p in self.medicine if p.__class__.__name__ == 'Painkiller']
        if painkiller_list:
            return painkiller_list
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        salves_list = [s for s in self.medicine if s.__class__.__name__ == 'Salves']
        if salves_list:
            return salves_list
        raise IndexError("There are no salves left!")

    def add_survivor(self, survivor: Survivor):
        for s in self.survivors:
            if s.name == survivor.name:
                raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type):
        to_remove_medicine = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
        if survivor.needs_healing:
            self.medicine.remove(to_remove_medicine)
            to_remove_medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        to_remove_sustain = [m for m in self.supplies if m.__class__.__name__ == sustenance_type][-1]
        if survivor.needs_sustenance:
            self.supplies.remove(to_remove_sustain)
            to_remove_sustain.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
        for survivor in self.survivors:
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')
