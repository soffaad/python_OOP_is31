class Vehicle:
    def move(self):
        print("Moving...")

    def fuel_type(self):
        print("Unknown")

class Car(Vehicle):
    def move(self):
        print("Driving...")

    def fuel_type(self):
        print("Petrol")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling...")

    def fuel_type(self):
        print("None")

vehicles = [Vehicle(), Car(), Bicycle()]
for v in vehicles:
    v.move()
    v.fuel_type()