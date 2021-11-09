import pytest as _
import terminal


def test_terminal_quick_exit(capsys, mocker):
    expected_output_list = [
        "Welcome to Gamestonk Terminal Beta",
        "Quick exit enabled",
    ]

    mocker.patch("terminal.gtff.ENABLE_QUICK_EXIT", return_value=True)

    terminal.terminal()

    captured = capsys.readouterr()

    for expected_output in expected_output_list:
        assert expected_output in captured.out


def test_terminal_quit(capsys, mocker):
    expected_output_list = [
        "Welcome to Gamestonk Terminal Beta",
    ]

    mocker.patch("builtins.input", return_value="quit")
    mocker.patch("terminal.session")
    mocker.patch("terminal.session.prompt", return_value="quit")
    mocker.patch("terminal.print_goodbye")

    spy_print_goodbye = mocker.spy(terminal, "print_goodbye")

    terminal.terminal()

    captured = capsys.readouterr()

    for expected_output in expected_output_list:
        assert expected_output in captured.out

    spy_print_goodbye.assert_called_once()
