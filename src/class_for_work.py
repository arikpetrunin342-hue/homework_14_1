class Product:
    name: str
    description: str
    price: float
    quality: int

    def __init__(self, name, description, price, quality):
        self.name = name
        self.description = description
        self.__price = price
        self.quality = quality

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quality} шт."

    def __add__(self, other):
        new_cost = self.__price * self.quality + other.__price * other.quality
        return new_cost

    @classmethod
    def new_product(cls, product_dict):
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевой или отрицательной.")
        else:
            self.__price = new_price


class Category:
    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        if products is None:
            self.__products = []
        else:
            self.__products = products[:]

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.product_count} шт."

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product.")
        Category.product_count += 1
        self.__products.append(product)

    def get_products(self):
        return self.__products.copy()

    @property
    def products(self):
        result = ""
        for prod in self.__products:
            line = (
                f"Продукт: {prod.name}, {prod.price} руб. Остаток: {prod.quality} шт."
            )
            result += line
        return result.strip()
