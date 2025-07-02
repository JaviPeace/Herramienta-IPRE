class Product:
    def cost(self):
        return 10

class TaxDecorator(Product):
    def __init__(self, product):
        self.product = product

    def cost(self):
        return self.product.cost() + 2

item = Product()
taxed_item = TaxDecorator(item)
print(taxed_item.cost())
