from typing import Any, Union

filename = None


def log(filename: Any) -> Any:
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
                        file.write(f"{func.__name__}.\nerror: {ex}.\nInputs: {args}.")
                else:
                    print(f"{func.__name__}.\nerror: {ex}.\nInputs: {args}.")

        return wrapper

    return decor


@log(filename="log.txt")
def my_function(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Функция возвращает результат сложения чисел"""
    return x + y


print(my_function(1, "2"))
