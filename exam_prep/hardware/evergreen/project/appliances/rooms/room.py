class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = []
    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self._expenses = value

    @property
    def cost(self):
        return self.expenses * 30 + self.room_cost

    def calculate_expenses(self, *args):
        self.expenses = sum((el.cost for seq in args for el in seq))



