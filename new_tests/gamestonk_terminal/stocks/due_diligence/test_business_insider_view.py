# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import business_insider_view
from gamestonk_terminal.stocks.stocks_helper import load


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_query_parameters": [
            ("period1", "1605481200"),
            ("period2", "1637103600"),
        ]
    }


@pytest.mark.vcr
def test_price_target_from_analysts_raw(capsys, default_txt_path):
    business_insider_view.price_target_from_analysts(
        ticker="TSLA",
        start=None,
        interval=None,
        stock=None,
        num=None,
        raw=True,
        export=None,
    )
    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()


@pytest.mark.default_cassette("test_price_target_from_analysts_TSLA")
@pytest.mark.vcr
@pytest.mark.parametrize("start", ["14/07/2020", None])
@pytest.mark.parametrize("interval", ["1440min", "60"])
def test_price_target_from_analysts_plt(capsys, interval, mocker, start):
    mock_show = mocker.Mock()
    mocker.patch(target="matplotlib.pyplot.show", new=mock_show)

    other_args = ["TSLA"]
    ticker = "TSLA"
    stock = pd.DataFrame()
    _ticker, _start, _interval, stock = load(
        other_args=other_args,
        s_ticker=ticker,
        s_start=start,
        s_interval=interval,
        df_stock=stock,
    )
    business_insider_view.price_target_from_analysts(
        ticker=ticker,
        start=start,
        interval=interval,
        stock=stock,
        num=None,
        raw=False,
        export=None,
    )
    _captured = capsys.readouterr()

    mock_show.assert_called_once()


@pytest.mark.vcr
def test_estimates(capsys, default_txt_path):
    business_insider_view.estimates(ticker="TSLA", export=None)
    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()
