class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Blue', 'Green', 'Black', 'White']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.model = model
        self.engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.capitalize() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

sedan1 = Sedan("Иван", "Toyota Camry", 180, "Red")
sedan1.print_info()
print("--- Попытка смены цвета ---")
sedan1.set_color("Black")
sedan1.print_info()
print("--- Попытка смены цвета на недопустимый ---")
sedan1.set_color("Yellow")
sedan1.print_info()