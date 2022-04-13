# create the class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    # assign fare
    def fare(self):
        return self.capacity * 100


# create bus class
# capacity is 50, with 10% extra maintenance charge
class Bus(Vehicle):
    def fare(self):
        return (self.capacity * 100) + (self.capacity * 100 * 0.10)


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

# check what type Bus is
print(type(School_bus))

# check instance
print(isinstance(School_bus, Vehicle))
