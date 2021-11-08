import pytest as _
import terminal

def test_terminal_quit(capsys, mocker):
    expected_output_list = {
        "goodbye": "!!!QUITTING THE TERMINAL PROPERLY!!!",
        "welcome": "Welcome to Gamestonk Terminal Beta",
    }

    mocker.patch("builtins.input", return_value="quit")
    mocker.patch("terminal.session")
    mocker.patch("terminal.session.prompt", return_value="quit")
    mocker.patch("terminal.print_goodbye", return_value=expected_output_list["goodbye"])

    terminal.terminal()

    captured = capsys.readouterr()

    for expected_output in expected_output_list:
        assert(expected_output in captured.out)
