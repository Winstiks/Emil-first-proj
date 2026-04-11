import time
import logging

# настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        duration = end - start

        logging.info(f"Функция {func.__name__} выполнена за {duration:.6f} секунд")

        return result

    return wrapper


# пример функции
@timer
def slow_function():
    time.sleep(1)
    return "Готово"


if __name__ == "__main__":
    slow_function()