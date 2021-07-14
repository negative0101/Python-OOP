class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type, ):
        cls.name = name
        cls.type = type
        return cls(name, type, 10)

    def add_item(self, item_name):
        if item_name not in self.items:
            self.items[item_name] = 1
            return f'{item_name} added to the shop'
        elif item_name in self.items and self.items[item_name] + 1 <= self.capacity:
            self.items[item_name] += 1
            return f'{item_name} added to the shop'

        else:
            return f'Not enough capacity in the shop'

    def remove_item(self, item_name, amount):
        if item_name in self.items:
            self.items[item_name] -= amount
            return f'{amount} {item_name} removed from the shop'
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


shop1 = Shop('Fresh', 'Fruit', 50)
shop2 = Shop.small_shop('Fashion', 'Clothing')
print(shop1)
print(shop2)
print(shop1.add_item('Bananas'))
print(shop1.remove_item('Tomatoes', 2))
print(shop2.add_item('Jeans'))
print(shop2.add_item('Jeans'))
print(shop2.remove_item('Jeans', 2))
