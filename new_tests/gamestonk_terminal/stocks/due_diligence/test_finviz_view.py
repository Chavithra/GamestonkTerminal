# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import finviz_view


@pytest.mark.parametrize(
    "val, expected",
    [
        ("RANDOM_VALUE", "RANDOM_VALUE"),
        ("Upgrade", "\x1b[32mUpgrade\x1b[0m"),
        ("Downgrade", "\x1b[31mDowngrade\x1b[0m"),
        ("Reiterated", "\x1b[33mReiterated\x1b[0m"),
    ],
)
def test_category_color_red_green(val, expected):
    result = finviz_view.category_color_red_green(val=val)
    assert result == expected


@pytest.mark.skip(reason="broken function and unused yet ")
@pytest.mark.vcr
def test_news(capsys, default_txt_path):
    finviz_view.news(ticker="TSLA", num=5)

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert expected_txt.strip() == captured.out.strip()


@pytest.mark.vcr
def test_analyst(capsys, default_txt_path):
    finviz_view.analyst(ticker="TSLA", export=None)

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert expected_txt.strip() == captured.out.strip()
