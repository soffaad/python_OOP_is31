
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

if __name__ == "__main__":
    animals = [Dog(), Cat(), Animal()]
    for a in animals:
        a.speak()  