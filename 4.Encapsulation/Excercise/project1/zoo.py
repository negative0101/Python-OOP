from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {type(animal).__name__} added to the zoo'

        elif len(self.animals) < self.__animal_capacity and self.__budget < price:
            return 'Not enough budget'

        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {type(worker).__name__} hired successfully'
        return f'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salary = sum(map(lambda worker: worker.salary, self.workers))
        if total_salary <= self.__budget:
            self.__budget -= total_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_money_for_care = sum(map(lambda animal: animal.money_for_care, self.animals))
        if total_money_for_care <= self.__budget:
            self.__budget -= total_money_for_care
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        res = f"You have {len(self.animals)} animals\n"

        lions = list(filter(lambda a: type(a) == Lion, self.animals))
        res = res + f"----- {len(lions)} Lions:\n"
        lions_info = "\n".join(repr(l) for l in lions)
        res += lions_info + '\n'

        tigers = list(filter(lambda a: type(a) == Tiger, self.animals))
        res = res + f"----- {len(tigers)} Tigers:\n"
        tigers_info = "\n".join(repr(t) for t in tigers)
        res += tigers_info + '\n'

        cheetahs = list(filter(lambda a: type(a) == Cheetah, self.animals))
        res = res + f"----- {len(cheetahs)} Cheetahs:\n"
        cheetahs_info = "\n".join(repr(c) for c in cheetahs)
        res += cheetahs_info

        return res

    def workers_status(self):
        res = f"You have {len(self.workers)} workers\n"

        keepers = list(filter(lambda a: type(a) == Keeper, self.workers))
        res = res + f"----- {len(keepers)} Keepers:\n"
        keepers_info = "\n".join(repr(k) for k in keepers)
        res += keepers_info + '\n'

        caretakers = list(filter(lambda a: type(a) == Caretaker, self.workers))
        res = res + f"----- {len(caretakers)} Caretakers:\n"
        caretakers_info = "\n".join(repr(t) for t in caretakers)
        res += caretakers_info + '\n'

        vets = list(filter(lambda a: type(a) == Vet, self.workers))
        res = res + f"----- {len(vets)} Vets:\n"
        vets_info = "\n".join(repr(c) for c in vets)
        res += vets_info

        return res
