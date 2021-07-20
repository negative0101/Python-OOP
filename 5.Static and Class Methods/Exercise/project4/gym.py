class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ''
        new_line = '\n'
        for i in range(len(self.subscriptions)):
            if self.subscriptions[i].id == subscription_id:
                result += f'{self.subscriptions[i]}'+ new_line
                result += f'{self.customers[i]}' + new_line
                result += f'{self.trainers[i]}' + new_line
                result += f'{self.equipment[i]}' + new_line
                result += f'{self.plans[i]}'

        return result