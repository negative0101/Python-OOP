from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable



class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0



    @property
    def name(self):
        return self.__name



    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value



    def add_food(self, food_type, name, price):
        for food in self.food_menu:
            if food.name == name and (food_type == 'Bread' or food_type == 'Cake'):
                raise Exception(f'{food_type} {name} is already in the menu!')
        if food_type == 'Bread':
            self.food_menu.append(Bread(name, price))
        elif food_type == 'Cake':
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"



    def add_drink(self, drink_type, name, portion, brand):
        for drink in self.drinks_menu:
            if drink.name == name and (drink_type == 'Tea' or drink_type == 'Water'):
                raise Exception(f'{drink_type} {name} is already in the menu!')
        if drink_type == 'Tea':
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == 'Water':
            self.drinks_menu.append(Water(name, portion, brand))
        return f"Added {name} ({drink_type}) to the drink menu"



    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == 'OutsideTable':
            self.tables_repository.append(OutsideTable(table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        # CHECK AGAIN FROM SELF.TABLE_REPOSITORY if doesn't work
        try:
            table_that_is_free = [t for t in self.tables_repository if t.is_reserved == False]
            for table_with_enough_space in table_that_is_free:
                if table_with_enough_space.capacity >= number_of_people:
                    table_with_enough_space.is_reserved = True
                    return f"Table {table_with_enough_space.table_number} has been reserved for {number_of_people} people"
        except IndexError:
            return f"No available table for {number_of_people} people"




    def order_food(self, table_number: int, *food_names):
        try:
            table_that_is_suitable = [t for t in self.tables_repository if t.table_number == table_number][0]
            foods_out_of_menu = []
            for food_n in food_names:
                for food in self.food_menu:
                    if food.name == food_n:
                        table_that_is_suitable.food_orders.append(food)
                foods_out_of_menu.append(food_n)
            result = f"Table {table_number} ordered:\n"
            new_line = '\n'
            for food in table_that_is_suitable.food_orders:
                result += new_line.join(f' - {food.name}: {food.portion}g - {food.portion}lv')
            result += f'{self.name} does not have in the menu:\n'
            for food in foods_out_of_menu:
                result += new_line.join(f'{food}')
        except:
            return f"Could not find table {table_number}"




    def order_drink(self, table_number: int, *drink_names):
        try:
            table_that_is_suitable = [t for t in self.tables_repository if t.table_number == table_number][0]
            drinks_out_of_menu = []
            for drinks_n in drink_names:
                for drink in self.drinks_menu:
                    if drink.name == drinks_n:
                        table_that_is_suitable.drink_orders.append(drink)
                drinks_out_of_menu.append(drinks_n)
            result = f"Table {table_number} ordered:\n"
            new_line = '\n'
            for drink in table_that_is_suitable.drink_orders:
                result += new_line.join(f'- {drink.name} {drink.brand} - {drink.portion}ml - {drink.price}lv')
            result += f'{self.name} does not have in the menu:\n'
            for drink in drinks_out_of_menu:
                result += new_line.join(f'{drink}')
        except IndexError:
            return f"Could not find table {table_number}"




    def leave_table(self, table_number: int):
        # not sure if it works
        total = 0


        for table in self.tables_repository:
            if table.table_number == table_number:
                for food in table.food_orders:
                    total += food.price
        for table in self.tables_repository:
            if table.table_number == table_number:
                for drink in table.drink_orders:
                    total += drink.price
            table.food_orders = []
            table.drink_orders = []
            table.is_reserved = False
        result = f"Table: {table_number}\n"
        result += f"Bill: {total:.2f}"
        return result




    def get_free_tables_info(self):
        res = '' # not needed , but could be done with it
        result = []
        new_line = '\n'
        for free_table in self.tables_repository:
            if not free_table.is_reserved:
                result.append(free_table)
        return new_line.join([i.free_table_info() for i in result])



    def get_total_income(self):
        income = 0
        for table in self.tables_repository:
            for i in table.food_orders:
                income+= i.price
            for j in table.drink_orders:
                income += j.price
        return f"Total income: {income:.2f}lv"

