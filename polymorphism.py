# Assignment 5
# Activity 2: Polymorphism Challenge 🎭

class Vehicle:
    def move(self):
        pass   # This will be overridden in subclasses


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")


class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water...")


# Demonstration of polymorphism
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        v.move()   # Each object runs its own move() method
