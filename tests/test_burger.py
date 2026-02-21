from tests.test_data import (
    TEST_BUN_PRICE,
    TEST_INGREDIENT_PRICE,
    TEST_BUN_NAME,
    TEST_INGREDIENT_NAME
)


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
    ing1 = object()
    ing2 = object()
    ing3 = object()

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.add_ingredient(ing3)

    burger.move_ingredient(2, 0)

    assert burger.ingredients[0] == ing3


def test_get_price(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(mock_ingredient)

    expected_price = TEST_BUN_PRICE * 2 + TEST_INGREDIENT_PRICE * 2
    assert burger.get_price() == expected_price


def test_get_receipt(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    receipt = burger.get_receipt()

    assert TEST_BUN_NAME in receipt
    assert TEST_INGREDIENT_NAME in receipt
