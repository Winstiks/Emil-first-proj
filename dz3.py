class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def play(self):
        self.happiness += 10
        print(f"{self.name} играет и становится счастливее 😊")

    def status(self):
        print(f"Питомец: {self.name}, Счастье: {self.happiness}")


class Human:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def work(self):
        self.energy -= 20
        print(f"{self.name} работает 😓")

    def rest(self):
        self.energy += 30
        print(f"{self.name} отдыхает 😌")

    def play_with_pet(self, pet):
        print(f"{self.name} играет с {pet.name}")
        pet.play()

    def status(self):
        print(f"Человек: {self.name}, Энергия: {self.energy}")


# --- Симуляция ---
human = Human("Алекс")
pet = Pet("Барсик")

human.status()
pet.status()

print("\n--- Действия ---")
human.work()
human.play_with_pet(pet)
human.rest()

print("\n--- Итог ---")
human.status()
pet.status()