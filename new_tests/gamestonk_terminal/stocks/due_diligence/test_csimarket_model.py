# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import csimarket_model


@pytest.mark.vcr
def test_get_suppliers(default_txt_path):
    result_txt = csimarket_model.get_suppliers(ticker="TSLA")

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert result_txt.strip() == expected_txt.strip()


@pytest.mark.vcr
def test_get_suppliers_invalid(default_txt_path):
    result_txt = csimarket_model.get_suppliers(ticker="INVALID_TICKER")

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert result_txt.strip() == expected_txt.strip()


@pytest.mark.vcr
def test_get_customers(default_txt_path):
    result_txt = csimarket_model.get_customers(ticker="TSLA")

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert result_txt.strip() == expected_txt.strip()


@pytest.mark.vcr
def test_get_customers_invalid(default_txt_path):
    result_txt = csimarket_model.get_customers(ticker="INVALID_TICKER")

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert result_txt.strip() == expected_txt.strip()
