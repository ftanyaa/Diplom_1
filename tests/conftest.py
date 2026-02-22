import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from tests.test_data import (
    TEST_BUN_NAME,
    TEST_BUN_PRICE,
    TEST_INGREDIENT_NAME,
    TEST_INGREDIENT_PRICE,
    TEST_INGREDIENT_TYPE
)


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = TEST_BUN_PRICE
    bun.get_name.return_value = TEST_BUN_NAME
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_price.return_value = TEST_INGREDIENT_PRICE
    ingredient.get_name.return_value = TEST_INGREDIENT_NAME
    ingredient.get_type.return_value = TEST_INGREDIENT_TYPE
    return ingredient
