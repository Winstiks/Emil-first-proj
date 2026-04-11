# --- Итератор, возвращающий генератор ---

class NumberCollection:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.generator()

    def generator(self):
        for i in range(self.start, self.end + 1):
            yield i


# --- Проверка ---
numbers = NumberCollection(1, 5)

print("Итерация по объекту:")
for num in numbers:
    print(num)


# --- Дополнительное задание: студент как итератор ---

import random


class StudentLife:
    def __init__(self, name, days):
        self.name = name
        self.days = days
        self.current_day = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_day >= self.days:
            raise StopIteration

        self.current_day += 1

        events = [
            "учился 📚",
            "спал 😴",
            "играл 🎮",
            "писал код 💻",
            "гулял 🚶"
        ]

        event = random.choice(events)
        return f"День {self.current_day}: {self.name} {event}"


# --- Проверка ---
student = StudentLife("Алекс", 5)

print("\nЖизнь студента:")
for day in student:
    print(day)