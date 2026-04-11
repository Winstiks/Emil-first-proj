import colorama
from colorama import Fore, Back, Style

# Инициализация
colorama.init()

print("=== Интроспекция модуля colorama ===")
print(dir(colorama))  # список всех атрибутов

print("\n=== Интроспекция Fore ===")
print(dir(Fore))

print("\n=== Интроспекция Back ===")
print(dir(Back))

print("\n=== Интроспекция Style ===")
print(dir(Style))


# Пример использования
print("\n=== Пример работы ===")
print(Fore.RED + "Красный текст")
print(Back.GREEN + "Зеленый фон")
print(Style.BRIGHT + "Яркий текст")
print(Style.RESET_ALL + "Сброс стилей")