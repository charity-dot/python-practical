# Task 1: Implementing Encapsulation

class Employee:
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid ID")
        self.__id = id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = salary

# Task 2: Implementing Inheritance and Polymorphism
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.started = False

    def start_engine(self):
        if not self.started:
            print(f"{self.make} {self.model} engine started")
            self.started = True
        else:
            print(f"{self.make} {self.model} engine is already started")

class Car(Vehicle):
    def start_engine(self):
        if not self.started:
            print(f"{self.make} {self.model} engine started with a vroom!")
            self.started = True
        else:
            print(f"{self.make} {self.model} engine is already started")

class Truck(Vehicle):
    def start_engine(self):
        if not self.started:
            print(f"{self.make} {self.model} engine started with a rumble!")
            self.started = True
        else:
            print(f"{self.make} {self.model} engine is already started")

def start_vehicle_engine(vehicle):
    vehicle.start_engine()

emp = Employee("John Doe", 123, 50000)
print(emp.get_name())  # Output: John Doe
emp.set_salary(60000)
print(emp.get_salary())  # Output: 60000

car = Car("Toyota", "Corolla")
truck = Truck("Ford", "F-150")

start_vehicle_engine(car)  # Output: Toyota Corolla engine started with a vroom!
start_vehicle_engine(truck)  # Output: Ford F-150 engine started with a rumble!

