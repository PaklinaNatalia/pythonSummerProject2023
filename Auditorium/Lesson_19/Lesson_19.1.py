class Car:
    def __init__(self, model, color, vin):
        self.model = model
        self.color = color
        self.vin = vin
    def __str__(self):
        return f"Модель: {self.model}\nЦвет: {self.color}\nVIN: {self.vin}"
    def __repr__(self):
        return f"Модель: {self.model}\nЦвет: {self.color}\nVIN: {self.vin}"

car_1 = Car("Mercedes", "silver", "N0000001")
car_1.__dict__["price"] = 1000000
for k, v in car_1.__dict__.items():
    print(f"{k}: {v}")
print()
car_2 = Car("BMW", "black", "N0000002")
Car.price = 1500000
car_3 = Car("Audi", "gold", "N0000003")
print(f"{car_1.model}: {car_1.price}\n{car_2.model}: {car_2.price}\n{car_3.model}: {car_3.price}")