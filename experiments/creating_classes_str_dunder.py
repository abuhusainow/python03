# mypy: ignore-errors
# flake8: noqa

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f"this is my brand of car: {self.brand}"

mine = Car("Ford", "black")
print(mine)
