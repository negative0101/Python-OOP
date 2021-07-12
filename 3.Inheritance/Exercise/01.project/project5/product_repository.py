
class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        products_with_that_name = [product.name for product in self.products if product.name == product_name]
        if products_with_that_name:
            return products_with_that_name[0]

    def remove(self, product_name):
        products_with_that_name = [product.name for product in self.products if product.name == product_name]
        self.products.remove(products_with_that_name[0])

    def __repr__(self):
        return "\n".join([f'{product.name}: {product.quantity}' for product in self.products])
