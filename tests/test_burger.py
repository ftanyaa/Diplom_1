import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = 100
    bun.get_name.return_value = "test bun"
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_price.return_value = 50
    ingredient.get_name.return_value = "test ingredient"
    ingredient.get_type.return_value = "SAUCE"
    return ingredient


def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_add_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients


def test_remove_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)

    assert len(burger.ingredients) == 0


def test_move_ingredient(burger):
    ing1 = Mock()
    ing2 = Mock()
    ing3 = Mock()

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.add_ingredient(ing3)

    burger.move_ingredient(2, 0)

    assert burger.ingredients[0] == ing3


def test_get_price(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(mock_ingredient)

    price = burger.get_price()

    assert price == 100 * 2 + 50 + 50


def test_get_receipt(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    receipt = burger.get_receipt()

    assert "test bun" in receipt
    assert "test ingredient" in receipt
    assert "Price:" in receipt
