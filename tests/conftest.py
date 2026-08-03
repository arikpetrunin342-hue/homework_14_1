import pytest

from src.class_for_work import Category, LawnGrass, Product, Smartphone

product1 = Product(
    "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

product_1 = Product(
    "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
)
product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

smartphone2 = Smartphone(
    "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
)

grass2 = LawnGrass(
    "Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый"
)


@pytest.fixture
def product():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def lawngrass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def category_emp_pr():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )


@pytest.fixture
def new_product():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_empty():
    """Создаёт пустую категорию."""
    return Category("Пустая", "")


@pytest.fixture
def category_emp_pr_zero_quantity():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)


@pytest.fixture
def category_with_products():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 1)
    return Category("Смартфоны", "дорогие", [product])


@pytest.fixture
def fail_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 0, 5)


@pytest.fixture
def category_2():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_2, product_3],
    )
