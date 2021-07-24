class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity >= len(self.animals) and self.__budget < price:
            return f'Not enough budget'
        else:
            return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        sum_of_worker_salaries = 0

        for worker in self.workers:
            sum_of_worker_salaries += worker.salary
        if self.__budget >= sum_of_worker_salaries:
            self.__budget -= sum_of_worker_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_of_money_for_care = 0
        for animal in self.animals:
            sum_of_money_for_care += animal.money_for_care
        if self.__budget >= sum_of_money_for_care:
            self.__budget -= sum_of_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        all_animals_count = 0
        result = ''

        all_lions = [lion for lion in self.animals if lion.__class__.__name__ == 'Lion']
        all_animals_count += len(all_lions)
        result += f'----- {len(all_lions)} Lions:\n'
        for lion in all_lions:
            result += repr(lion) + '\n'
        all_tigers = [tiger for tiger in self.animals if tiger.__class__.__name__ == 'Tiger']
        all_animals_count += len(all_tigers)
        result += f'----- {len(all_tigers)} Tigers:\n'
        for tiger in all_tigers:
            result += repr(tiger) + '\n'
        all_cheetahs = [cheetah for cheetah in self.animals if cheetah.__class__.__name__ == 'Cheetah']
        all_animals_count += len(all_cheetahs)

        result += f'----- {len(all_cheetahs)} Cheetahs:\n'

        result += '\n'.join([repr(cheetah) for cheetah in all_cheetahs])

        all_animals = f'You have {all_animals_count} animals\n'
        result = all_animals + result

        return result

    def workers_status(self):
        all_workers_count = 0
        result = ''

        all_keepers = [keepers for keepers in self.workers if keepers.__class__.__name__ == 'Keeper']
        all_workers_count += len(all_keepers)
        result += f'----- {len(all_keepers)} Keepers:\n'
        for keeper in all_keepers:
            result += repr(keeper) + '\n'

        all_caretakers = [caretakers for caretakers in self.workers if caretakers.__class__.__name__ == 'Caretaker']
        all_workers_count += len(all_caretakers)
        result += f'----- {len(all_caretakers)} Caretakers:\n'
        for caretaker in all_caretakers:
            result += repr(caretaker) + '\n'

        all_vets = [vet for vet in self.workers if vet.__class__.__name__ == 'Vet']
        all_workers_count += len(all_vets)
        result += f'----- {len(all_vets)} Vets:\n'

        result += '\n'.join([repr(vet) for vet in all_vets])

        all_workers = f'You have {all_workers_count} workers\n'
        result = all_workers + result

        return result
