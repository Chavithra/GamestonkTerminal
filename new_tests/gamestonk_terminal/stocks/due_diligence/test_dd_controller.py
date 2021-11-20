# IMPORTATION STANDARD
import os

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import dd_controller

# pylint: disable=E1101

first_call = True


@pytest.mark.block_network
def test_menu_quick_exit(capsys, default_txt_path, mocker):
    mocker.patch("builtins.input", return_value="quit")
    mocker.patch("gamestonk_terminal.stocks.due_diligence.dd_controller.session")
    mocker.patch(
        "gamestonk_terminal.stocks.due_diligence.dd_controller.session.prompt",
        return_value="quit",
    )

    stock = pd.DataFrame()
    dd_controller.menu(
        ticker="TSLA", start="10/25/2021", interval="1440min", stock=stock
    )

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()


@pytest.mark.block_network
def test_menu_system_exit(capsys, default_txt_path, mocker):
    global first_call
    first_call = True

    def side_effect(arg):
        global first_call
        if first_call:
            first_call = False
            raise SystemExit()

        return arg

    m = mocker.Mock(return_value="quit", side_effect=side_effect)
    mocker.patch("builtins.input", return_value="quit")
    mocker.patch("gamestonk_terminal.stocks.due_diligence.dd_controller.session")
    mocker.patch(
        "gamestonk_terminal.stocks.due_diligence.dd_controller.session.prompt",
        return_value="quit",
    )
    mocker.patch(
        "gamestonk_terminal.stocks.due_diligence.dd_controller.DueDiligenceController.switch",
        new=m,
    )

    stock = pd.DataFrame()
    dd_controller.menu(
        ticker="TSLA", start="10/25/2021", interval="1440min", stock=stock
    )

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()


@pytest.mark.block_network
def test_print_help(capsys, default_txt_path):
    dd = dd_controller.DueDiligenceController(
        ticker="", start="", interval="", stock=pd.DataFrame()
    )
    dd.print_help()

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()


@pytest.mark.block_network
def test_switch_empty(capsys, default_txt_path):
    dd = dd_controller.DueDiligenceController(
        ticker="", start="", interval="", stock=pd.DataFrame()
    )
    result = dd.switch(an_input="")

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert result is None
    assert captured.out.strip() == expected_txt.strip()


@pytest.mark.block_network
def test_switch_help(capsys, default_txt_path):
    dd = dd_controller.DueDiligenceController(
        ticker="", start="", interval="", stock=pd.DataFrame()
    )
    result = dd.switch(an_input="?")

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert result is None
    assert captured.out.strip() == expected_txt.strip()


@pytest.mark.block_network
def test_switch_cls(capsys, default_txt_path, mocker):
    mocker.patch("os.system")
    dd = dd_controller.DueDiligenceController(
        ticker="", start="", interval="", stock=pd.DataFrame()
    )
    result = dd.switch(an_input="cls")

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert result is None
    assert captured.out.strip() == expected_txt.strip()
    os.system.assert_called_once_with("cls||clear")


@pytest.mark.block_network
def test_call_q():
    dd = dd_controller.DueDiligenceController(
        ticker="", start="", interval="", stock=pd.DataFrame()
    )
    other_args = list()
    result = dd.call_q(other_args)

    assert result is False


@pytest.mark.block_network
def test_call_quit():
    dd = dd_controller.DueDiligenceController(
        ticker="", start="", interval="", stock=pd.DataFrame()
    )
    other_args = list()
    result = dd.call_quit(other_args)

    assert result is True


@pytest.mark.block_network
def test_call_load_no_args(capsys):
    dd = dd_controller.DueDiligenceController(
        ticker="TSLA", start="10/25/2021", interval="1440min", stock=pd.DataFrame()
    )
    other_args = list()
    dd.call_load(other_args)
    _captured = capsys.readouterr()


@pytest.mark.block_network
@pytest.mark.parametrize(
    "tested_func, mocked_func, other_args, called_with",
    [
        (
            "call_analyst",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.finviz_view.analyst",
            [],
            {"ticker": "TSLA", "export": ""},
        ),
        (
            "call_analyst",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.finviz_view.analyst",
            ["--export=csv"],
            {"ticker": "TSLA", "export": "csv"},
        ),
        (
            "call_analyst",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.finviz_view.analyst",
            ["--export=json"],
            {"ticker": "TSLA", "export": "json"},
        ),
        (
            "call_analyst",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.finviz_view.analyst",
            ["--export=xlsx"],
            {"ticker": "TSLA", "export": "xlsx"},
        ),
        (
            "call_pt",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.business_insider_view.price_target_from_analysts",
            ["--num=10"],
            {
                "ticker": "TSLA",
                "start": "10/25/2021",
                "interval": "1440min",
                "stock": None,
                "num": 10,
                "raw": False,
                "export": "",
            },
        ),
        (
            "call_est",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.business_insider_view.estimates",
            [],
            {
                "ticker": "TSLA",
                "export": "",
            },
        ),
        (
            "call_rot",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.finnhub_view.rating_over_time",
            ["--num=10"],
            {
                "ticker": "TSLA",
                "num": 10,
                "raw": False,
                "export": "",
            },
        ),
        (
            "call_rating",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.fmp_view.rating",
            ["--num=10"],
            {
                "ticker": "TSLA",
                "num": 10,
                "export": "",
            },
        ),
        (
            "call_sec",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.marketwatch_view.sec_filings",
            ["--num=10"],
            {
                "ticker": "TSLA",
                "num": 10,
                "export": "",
            },
        ),
        (
            "call_supplier",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.csimarket_view.suppliers",
            [],
            {
                "ticker": "TSLA",
                "export": "",
            },
        ),
        (
            "call_arktrades",
            "gamestonk_terminal.stocks.due_diligence.dd_controller.ark_view.display_ark_trades",
            ["--num=10", "-s"],
            {
                "ticker": "TSLA",
                "num": 10,
                "export": "",
                "show_ticker": True,
            },
        ),
    ],
)
def test_call_func(tested_func, mocked_func, other_args, called_with, mocker):
    mock = mocker.Mock()
    mocker.patch(mocked_func, new=mock)
    dd = dd_controller.DueDiligenceController(
        ticker="TSLA",
        start="10/25/2021",
        interval="1440min",
        stock=None,
    )
    getattr(dd, tested_func)(other_args=other_args)

    if called_with:
        mock.assert_called_once_with(**called_with)
    else:
        mock.assert_called_once()


@pytest.mark.block_network
@pytest.mark.parametrize(
    "func",
    [
        "call_analyst",
        "call_pt",
        "call_est",
        "call_rot",
        "call_rating",
        "call_sec",
        "call_supplier",
        "call_customer",
        "call_arktrades",
    ],
)
def test_call_func_no_parser(func, mocker):
    mocker.patch(
        "gamestonk_terminal.stocks.due_diligence.dd_controller.parse_known_args_and_warn",
        return_value=None,
    )
    dd = dd_controller.DueDiligenceController(
        ticker="AAPL", start="10/25/2021", interval="1440min", stock=pd.DataFrame()
    )

    func_result = getattr(dd, func)(other_args=list())
    assert func_result is None
    getattr(dd_controller, "parse_known_args_and_warn").assert_called_once()
