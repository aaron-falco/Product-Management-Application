class Products:
    def __init__(self, products=[]):
        self.products = products
    
    def get_all_products(self):
        return self.products
    
    def get_available_products(self):
        return [product for product in self.products if product.is_available()]
    
    def remove_product(self, product):
        self.products.remove(product)

    def remove_product(self, product):
        self.products.remove(product)