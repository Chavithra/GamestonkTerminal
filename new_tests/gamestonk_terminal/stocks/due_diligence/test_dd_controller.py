# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import dd_controller


@pytest.mark.vcr
def test_menu_quick_exit(capsys, mocker):
    mocker.patch("builtins.input", return_value="quit")
    mocker.patch("gamestonk_terminal.stocks.due_diligence.dd_controller.session")
    mocker.patch("gamestonk_terminal.stocks.due_diligence.dd_controller.session.prompt", return_value="quit")

    stock = pd.DataFrame()
    dd_controller.menu(ticker="TSLA", start="10/25/2021", interval="1440min", stock=stock)

    captured = capsys.readouterr()

    print(captured.out)