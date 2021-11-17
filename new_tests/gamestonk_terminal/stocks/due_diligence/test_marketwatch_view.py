# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import marketwatch_view


@pytest.mark.vcr
def test_analyst(capsys, default_txt_path):
    marketwatch_view.sec_filings(ticker="TSLA", num=5, export=None)

    captured = capsys.readouterr()

    # with open(file=default_txt_path, mode="w", encoding="utf-8") as f:
    #     f.write(captured.out)
    with open(file=default_txt_path, mode="r", encoding="utf-8") as f:
        expected_txt = f.read()

    assert expected_txt.strip() == captured.out.strip()
