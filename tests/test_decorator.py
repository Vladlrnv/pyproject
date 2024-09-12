from typing import Any

from src.decorator import log


def test_log_without_txt(capsys: Any) -> Any:
    """Тестирует вывод данных в консоль при удачном выполнении функиции my_function"""

    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok.\n"
    assert my_function(1, 2) == 3


def test_log_with_txt() -> Any:
    """Тестирует вывод данных в текстовый документ при удачном выполнении функиции my_function"""

    @log(filename="log.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    with open("log.txt", "r") as file:
        content = file.read()
    assert "my_function ok." in content
    assert my_function(1, 2) == 3


def test_log_without_txt_error(capsys: Any) -> Any:
    """Тестирует вывод данных в консоль при возникновении ошибки в выполнении функиции my_function"""

    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function.\nerror: "
           "test_log_without_txt_error.<locals>.my_function() missing 1 required positional argument: 'y'.\nInputs: "
           "(1,).\n"
    )


def test_log_with_txt_error() -> Any:
    """Тестирует вывод данных в текстовый документ при отсутствии одного из параметров функиции my_function"""

    @log(filename="log.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1)
    with open("log.txt", "r") as file:
        content = file.read()
    assert (
        "my_function.\nerror: "
        "test_log_with_txt_error.<locals>.my_function() missing 1 required positional argument: 'y'.\nInputs: (1,)."
        in content
    )


def test_log_with_txt_error_str() -> Any:
    @log(filename="log.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, "2")
    with open("log.txt", "r") as file:
        content = file.read()
    assert "my_function.\nerror: unsupported operand type(s) for +: 'int' and 'str'.\nInputs: (1, '2')." in content
    assert my_function(1, "2") is None
