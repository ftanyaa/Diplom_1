from unittest.mock import patch
from praktikum.praktikum import main


def test_main_runs_without_errors():
    with patch("builtins.print") as mock_print:
        main()
        assert mock_print.called
