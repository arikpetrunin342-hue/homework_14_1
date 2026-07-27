import pytest

from src.class_for_work import Product, Category

@pytest.fixture
def product():
    return Product('tomato', 'red', 15.50, 10)

@pytest.fixture
def category():
    return Category('for salad', 'good salad', ['tomato', 'cucumber', 'salt', 'onion', 'sour cream'])
