
from src.class_for_work import Category


def test_products(product):
    assert product.name == 'tomato'
    assert product.description == 'red'
    assert product.price == 15.50
    assert product.quantity == 10


def test_category(category):
    assert isinstance(category, Category)
    assert category.name == 'for salad'
    assert category.description == 'good salad'
    assert category.category_count == 1
    assert category.product_count == 5

