from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор логирует начало и конец выполнения декорируемой функции, а также ее результаты или возникшие ошибки"""

    def decor(func: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok.")
                else:
                    print(f"{func.__name__} ok.")
                return result
            except Exception as ex:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__}.\nerror: {ex}.\nInputs: {args}, {kwargs}.")
                else:
                    print(f"{func.__name__}.\nerror: {ex}.\nInputs: {args}, {kwargs}.")

        return wrapper

    return decor


@log()
def my_function(x: Any, y: Any) -> Any:
    """Функция возвращает результат сложения чисел"""
    return x + y


print(my_function(1, "2"))
