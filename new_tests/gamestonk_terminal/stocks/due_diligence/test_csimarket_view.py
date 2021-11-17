# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import csimarket_view


@pytest.mark.vcr
def test_get_suppliers(capsys, default_txt_path):
    csimarket_view.suppliers(ticker="TSLA", export=None)

    captured = capsys.readouterr()

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()

@pytest.mark.vcr
def test_get_suppliers_invalid(capsys, default_txt_path):
    csimarket_view.suppliers(ticker="INVALID_TICKER", export=None)

    captured = capsys.readouterr()

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()


@pytest.mark.vcr
def test_get_customers(capsys, default_txt_path):
    csimarket_view.customers(ticker="TSLA", export=None)

    captured = capsys.readouterr()

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()


@pytest.mark.vcr
def test_get_customers_invalid(capsys, default_txt_path):
    csimarket_view.customers(ticker="INVALID_TICKER", export=None)

    captured = capsys.readouterr()

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()