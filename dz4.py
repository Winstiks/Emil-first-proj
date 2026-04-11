class Worker:
    def __init__(self, job):
        self.job = job

    def work(self):
        print(f"Работает как {self.job}")


class Student:
    def __init__(self, university):
        self.university = university

    def study(self):
        print(f"Учится в {self.university}")


class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def train(self):
        print(f"Тренируется в {self.sport}")


# Множественное наследование
class Person(Worker, Student, Athlete):
    def __init__(self, name, job, university, sport):
        self.name = name

        # вызываем конструкторы родителей
        Worker.__init__(self, job)
        Student.__init__(self, university)
        Athlete.__init__(self, sport)

    def introduce(self):
        print(f"Меня зовут {self.name}")

    def full_info(self):
        self.introduce()
        self.work()
        self.study()
        self.train()


# --- Проверка ---
person = Person("Алекс", "программист", "БГУ", "футбол")

person.full_info()