# PLP Python Week 5 OOP Assignment
# Contains:
# 1. A Smartphone class (Inheritance & Encapsulation)
# 2. A Vehicle example (Polymorphism)

# -------------------------------
# Part 1: Smartphone Class 🏗️
# -------------------------------

# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    # Method (behavior)
    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}...")

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"{self.device_info()} charged to {self.battery}%.")


# -------------------------------
# Part 2: Polymorphism Challenge 🎭
# -------------------------------

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


# -------------------------------
# Demonstration of Both Parts
# -------------------------------
if __name__ == "__main__":
    print("=== Part 1: Smartphone Class ===")
    phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 50)
    phone2 = Smartphone("Apple", "iPhone 15", "512GB", 80)

    phone1.make_call("08012345678")
    phone1.charge(30)

    phone2.make_call("08123456789")
    phone2.charge(50)

    print("\n=== Part 2: Polymorphism with Vehicles ===")
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        v.move()
