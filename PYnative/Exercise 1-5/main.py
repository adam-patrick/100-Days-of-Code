class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity


def seating_capacity(self, capacity=50):
    return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    pass


def Details(self):
    print(f"Details: Name: {self.name} Color: {self.color} Mileage: {self.mileage} Capacity: {self.capacity}.")


School_bus = Bus("School Volvo", 180, 12, 50)
Details(School_bus)
