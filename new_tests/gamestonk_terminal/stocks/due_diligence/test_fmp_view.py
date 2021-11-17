# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import fmp_view

@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_query_parameters": [
            ("apikey", "MOCK_API_KEY"),
        ]
    }


@pytest.mark.vcr
def test_rating(capsys, default_txt_path):
    fmp_view.rating(ticker="TSLA", num=5, export=None)

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert expected_txt.strip() == captured.out.strip()
