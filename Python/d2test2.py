from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, m, b):
        self.model = m
        self.brand = b

    def info(self):
        return self.model + " " + self.brand
    
    @abstractmethod
    def driving(self):
        pass

class Bike(Vehicle):
    def __init__(self, m, b):
        # super().__init__(m, b)
        self.__price = 100000
        self.color = "Black"
        self._c = 100

    def getPrice(self):
        return self.__price

    def setPrice(self, p):
        self.__price = p

    def info(self):
        return self.model + " " + self.brand + " " + self.color + " " + str(self.__price) + " " + str(self._c)
    def driving(self):
        print("Yes i am driving bike")




obj = Bike("Yamaha", "R15")
print(obj.color)
print(obj.getPrice())
obj.setPrice(200000)

print(obj.getPrice())
print(obj.info())

# obj1 = Vehicle("Tata", "Punch")
# print(obj1.info())

print(obj.driving())