Курс: Искусственный интеллект
и большие данные
(Программирование на Python - Senior)

Тема: Исключения. Генерация и обработка
исключений. Предупреждение

Задание
Сделайте так, чтобы программа работала, а все типы исклю-
чений выводились в консоль.
Результат работы разместите на GitHub.
Код программы:

result = []
def divider(a, b):
if a < b:
raise ValueError
if b > 100:
raise IndexError
return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}

for key in data:
res = divider(key, data[kem])
result.append(res)

print(result)

1