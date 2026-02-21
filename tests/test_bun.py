import pytest
from praktikum.bun import Bun
from tests.test_data import TEST_BUN_NAME, TEST_BUN_NAMES, TEST_PRICES


@pytest.mark.parametrize("name", TEST_BUN_NAMES)
def test_get_name_returns_correct_name(name):
    bun = Bun(name, 100)
    assert bun.get_name() == name


@pytest.mark.parametrize("price", TEST_PRICES)
def test_get_price_returns_correct_price(price):
    bun = Bun(TEST_BUN_NAME, price)
    assert bun.get_price() == price

