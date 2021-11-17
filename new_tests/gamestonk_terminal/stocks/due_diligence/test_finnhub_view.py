# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import finnhub_view

@pytest.mark.default_cassette("test_rating_over_time_TSLA")
@pytest.mark.vcr
def test_rating_over_time(capsys, default_txt_path):
    finnhub_view.rating_over_time(
        ticker="TSLA",
        num=10,
        raw=True,
        export=None,
    )
    captured = capsys.readouterr()

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()


@pytest.mark.default_cassette("test_rating_over_time_TSLA")
@pytest.mark.vcr(mode="none")
def test_rating_over_time_plt(capsys, mocker):
    mock_show = mocker.Mock()
    mocker.patch(target="matplotlib.pyplot.show", new=mock_show)
    finnhub_view.rating_over_time(
        ticker="TSLA",
        num=10,
        raw=False,
        export=None,
    )

    _captured = capsys.readouterr()

    mock_show.assert_called_once()


@pytest.mark.vcr
def test_rating_over_time_invalid_ticker(capsys, default_txt_path):
    finnhub_view.rating_over_time(
        ticker="INVALID_TICKER",
        num=10,
        raw=False,
        export=None,
    )

    captured = capsys.readouterr()

    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert captured.out.strip() == expected_txt.strip()
