import io

import pytest

from src.class_for_work import Category, Product


@pytest.fixture
def empty_category():
    return Category("Пустая", "Описание")


def test_products(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


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


def test_category_products(empty_category):
    result = empty_category.products
    assert isinstance(result, str)
    assert (
        "" in result.lower()
    ), "Для пустых категорий должно быть соответствующее сообщение."

    product = Product("Кофе", "Арабика", 600, 7)
    empty_category.add_product(product)
    result = empty_category.products
    assert (
        "Продукт: Кофе, 600 руб. Остаток: 7 шт." in result
    ), "Свойство должно вернуть корректную информацию о товаре."


def test_category(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category.category_count == 1
    assert category.product_count == 3


def test_category_add_product(category):
    new_item = Product.new_product(
        {
            "name": "Test Phone",
            "description": "Just a phone.",
            "price": 10_000,
            "quality": 3,
        }
    )

    category.add_product(new_item)

    assert (
        len(category.get_products()) == 4
    ), f"Ожидалось 4 продукта, а в категории {len(category.get_products())}."

    assert (
        category.product_count == 4
    ), f"Счётчик product_count неверный: ожидалось 4, получено {category.product_count}"


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

