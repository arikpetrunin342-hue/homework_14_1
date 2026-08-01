import io

import pytest

from src.class_for_work import Category, LawnGrass, Product, Smartphone


class New:
    def __init__(self, name):
        self.name = name


def test_products(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_products_add():
    prod_1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    prod_2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    res_prod = prod_1 + prod_2
    assert str(res_prod) == "2114000.0"
    with pytest.raises(TypeError):
        _ = prod_1 + grass2


def test_price_property(product):
    initial_price = product.price
    assert initial_price == 180_000.0, f"Ожидалось 180000.0, получено {initial_price}"

    product.price = 150_000.0
    updated_price = product.price
    assert (
        updated_price == 150_000.0
    ), f"Цена не обновилась: ожидалось 150000.0, получено {updated_price}"

    from contextlib import redirect_stdout

    with io.StringIO() as buf, redirect_stdout(buf):
        product.price = 0
        output = buf.getvalue().strip()

    assert (
        output == "Цена не должна быть нулевой или отрицательной."
    ), f"Не выведено сообщение об ошибке, а '{output}'"

    unchanged_price = product.price
    assert (
        unchanged_price == 150_000.0
    ), f"После ошибки цена изменилаcь! Ожидалось 150000.0, получено {unchanged_price}"

    with io.StringIO() as buf, redirect_stdout(buf):
        product.price = -100
        output = buf.getvalue().strip()

    assert (
        output == "Цена не должна быть нулевой или отрицательной."
    ), f"Не выведено сообщение об ошибке, а '{output}'"

    try:
        product.price = "abc"
    except TypeError:
        pass
    else:
        raise AssertionError("Должна была возникнуть ошибка преобразования типа.")


def test_price_property_negative(product):
    """Проверка реакции при попытке установить отрицательную цену."""

    initial_price = product.price
    product.price = -1
    assert (
        product.price == initial_price
    ), "Цена изменилась при установке отрицательного значения."


def test_price_property_zero(product):
    """Проверка реакции при попытке установить нулевую цену."""

    initial_price = product.price
    product.price = 0
    assert product.price == initial_price, "Цена изменилась при установке нуля."


def test_category_products(category):
    result = category.products
    assert isinstance(result, str)
    assert (
        "" in result.lower()
    ), "Для пустых категорий должно быть соответствующее сообщение."

    product = Product("Кофе", "Арабика", 600, 7)
    category.add_product(product)
    result = category.products
    assert (
        "Продукт: Кофе, 600 руб. Остаток: 7 шт." in result
    ), "Свойство должно вернуть корректную информацию о товаре."


def test_category(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    expected = "Смартфоны, количество продуктов: 27 шт."
    assert category.category_count == 1
    assert category.product_count == 3
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."
    assert str(category) == expected


def test_category_add_product(category):
    new_item = Product.new_product(
        {
            "name": "Test Phone",
            "description": "Just a phone.",
            "price": 10_000,
            "quantity": 3,
        }
    )

    category.add_product(new_item)

    assert (
        len(category.get_products()) == 4
    ), f"Ожидалось 4 продукта, а в категории {len(category.get_products())}."

    assert (
        category.product_count == 4
    ), f"Счётчик product_count неверный: ожидалось 4, получено {category.product_count}"

    new = New("name")

    with pytest.raises(TypeError):
        _ = new_item + new


def test_category_get_products(category):
    products_copy = category.get_products()

    assert isinstance(products_copy, list), "Метод должен вернуть список."

    original_list = category._Category__products
    products_copy.append("Fake Product")
    assert len(original_list) != len(
        products_copy
    ), "Возвращённый список является ссылкой на оригинальный!"

    assert isinstance(products_copy, list)
    assert products_copy is not original_list, "Возвращён оригинал вместо копии!"


def test_category_empty():

    empty_category = Category("Пустая", "Описание пустой")
    products = empty_category.get_products()

    assert isinstance(
        products, list
    ), "Метод должен вернуть список даже для пустой категории."
    assert not products, "Список товаров не должен быть пустым."
    assert empty_category.product_count == 0, "Счётчик товаров должен быть равен нулю."


def test_smartphone(smartphone):
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawngrass(lawngrass):
    assert lawngrass.name == "Газонная трава"
    assert lawngrass.description == "Элитная трава для газона"
    assert lawngrass.price == 500.0
    assert lawngrass.quantity == 20
    assert lawngrass.country == "Россия"
    assert lawngrass.germination_period == "7 дней"
    assert lawngrass.color == "Зеленый"


def test_add_same_type_product(product):
    """Проверяет, что сумма двух смартфонов верна."""
    prod_1 = Product("iPhone", "Blue", 50000.0, 4)
    prod_2 = Product("Samsung", "White", 60000.0, 3)
    result = prod_1 + prod_2
    expected_sum = 50000.0 * 4 + 60000.0 * 3  # 200k + 180k = 380k
    assert result == expected_sum, f"{result} != {expected_sum}"


def test_add_different_classes():
    """Проверяет, что нельзя сложить продукт и газонную траву."""
    product = Product("Смартфон", "Мощный", 10000.0, 1)
    grass = LawnGrass(
        "Газонная трава",
        "Выносливая трава",
        450.0,
        15,
        "Россия",
        "5 дней",
        "Темно-зеленый",
    )
    with pytest.raises(TypeError):
        _ = product + grass


def test_add_invalid_types():
    """Проверяет, что нельзя сложить продукт со строкой/числом/None."""
    product = Product("Товар", "Хороший", 100.0, 1)

    with pytest.raises(TypeError):
        _ = product + 100

    with pytest.raises(TypeError):
        _ = product + "Строка"

    with pytest.raises(TypeError):
        _ = product + None


def test_add_self():
    product = Product("Товар", "Хороший", 1.0, 1)
    res = product + product
    assert res == 2.0


@pytest.fixture
def category_empty():
    """Создаёт пустую категорию."""
    return Category("Пустая", "")


def test_inheritance():
    """Проверяет наличие базовых свойств в дочерних классах."""
    sp = Smartphone("Test", "", 100.0, 1, 100.0, "", 1, "")
    lg = LawnGrass("Test", "", 100.0, 1, "", "", "")

    assert hasattr(sp, "name") and isinstance(sp.name, str)
    assert hasattr(lg, "price") and isinstance(lg.price, float)

    assert hasattr(sp, "memory") and isinstance(sp.memory, int)
    assert hasattr(lg, "country") and isinstance(lg.country, str)


def test_add_product_to_list(category_emp_pr):
    product = Product("Товар", "Описание", 100.0, 1)
    category_emp_pr.add_product(product)

    products_copy = category_emp_pr.get_products()
    assert len(products_copy) == 1, "Список товаров должен был пополниться."
    assert product is products_copy[0], "Добавленный товар найден в списке"
