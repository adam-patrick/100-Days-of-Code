def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 4, 5, 6, 7, 8, 9, 10))


def calculate(**kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seats = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
