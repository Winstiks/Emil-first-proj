import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100  # начальный баланс
        self.knowledge = 50  # уровень знаний (0-100)
        self.energy = 100  # энергия (0-100)
        self.mood = 100  # настроение (0-100)
        self.day = 0

    def study(self):
        print("📚 Учёба...")
        self.knowledge += 10
        self.energy -= 15
        self.mood -= 5
        self._normalize()

    def work(self):
        print("💼 Работа...")
        self.money += 50
        self.energy -= 20
        self.mood -= 10
        self._normalize()

    def rest(self):
        print("🎮 Отдых...")
        self.energy += 20
        self.mood += 15
        self.money -= 20
        self._normalize()

    def live_day(self):
        print(f"\n📅 День {self.day}")
        print(f"💰 Деньги: {self.money} | 📚 Знания: {self.knowledge} | ⚡ Энергия: {self.energy} | 😊 Настроение: {self.mood}")

        # Логика поведения
        if self.money < 20:
            self.work()
        elif self.knowledge < 40:
            self.study()
        elif self.energy < 30:
            self.rest()
        else:
            action = random.choice([self.study, self.work, self.rest])
            action()

        self.day += 1

    def is_alive(self):
        if self.energy <= 0:
            print("😵 Студент умер от усталости...")
            return False
        if self.mood <= 0:
            print("😭 Студент впал в депрессию...")
            return False
        if self.knowledge <= 0:
            print("📉 Студента отчислили...")
            return False
        if self.money <= -100:
            print("💸 Студент в огромных долгах...")
            return False
        return True

    def _normalize(self):
        self.energy = max(0, min(100, self.energy))
        self.mood = max(0, min(100, self.mood))
        self.knowledge = max(0, min(100, self.knowledge))


# Симуляция года (365 дней)
student = Student("Алекс")

for _ in range(365):
    if not student.is_alive():
        break
    student.live_day()
else:
    print("\n🎉 Студент успешно прожил год!")