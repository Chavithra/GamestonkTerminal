# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import ark_view


@pytest.mark.default_cassette("test_display_ark_trades_INVALID_TICKER")
@pytest.mark.vcr(record_mode="none")
def test_display_ark_trades_invalid_ticker(capsys):
    ark_view.display_ark_trades(ticker="INVALID_TICKER")

    captured = capsys.readouterr()

    expected_output = (
        "Issue getting data from cathiesark.com.  Likely no trades found.\n"
    )
    assert expected_output in captured.out


@pytest.mark.default_cassette("test_display_ark_trades_TSLA")
@pytest.mark.vcr(record_mode="none")
def test_display_ark_trades_default(capsys, default_txt_path):
    ark_view.display_ark_trades(ticker="TSLA")

    captured = capsys.readouterr()

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert expected_txt.strip() == captured.out.strip()


@pytest.mark.default_cassette("test_display_ark_trades_TSLA")
@pytest.mark.vcr(record_mode="none")
def test_display_ark_trades_no_tab(capsys, default_txt_path, mocker):
    mocker.patch(
        target="gamestonk_terminal.feature_flags.USE_TABULATE_DF",
        new=False,
    )

    ark_view.display_ark_trades(ticker="TSLA")

    captured = capsys.readouterr()

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert expected_txt.strip() == captured.out.strip()


@pytest.mark.default_cassette("test_display_ark_trades_TSLA")
@pytest.mark.vcr(record_mode="none")
def test_display_ark_trades_export(capsys, mocker):
    ark_view.export_data = mocker.Mock()

    ark_view.display_ark_trades(ticker="TSLA", export="csv")
    _captured = capsys.readouterr()

    ark_view.export_data.assert_called_once()
