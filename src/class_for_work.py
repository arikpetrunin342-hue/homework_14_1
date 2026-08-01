class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            new_cost = self.__price * self.quantity + other.__price * other.quantity
            return new_cost
        else:
            raise TypeError

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
        return f"{self.name}, количество продуктов: {sum(p.quantity for p in self.__products)} шт."

    def __len__(self):
        return len(f"{self.products}")

    def add_product(self, product: Product):
        if not issubclass(type(product), Product):
            raise TypeError("Можно добавлять только продукты или их наследники!")
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
                f"Продукт: {prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт."
            )
            result += line
        return result.strip()


class Smartphone(Product):  #

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):  #

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
