# 13Class.py
"""
public class Car
{
    필드...
    생성자...
    메소드...
}
"""

class Car:
    # 필드 (클래스 내의 변수)
    color = str()

    # 메소드
    def printCar(self):                 # 파라미터가 없으면 안되는 경우, self가 들어감
        print("color = ", self.color)   # Java의 this.color과 동일


taxi = Car()    # class Car에 생성자 없었으니까 디폴트생성자 이용~
print(type(taxi))
taxi.color = "red"
taxi.printCar()

print("-" * 80)

class MyCar:
    def __init__(self, name, color, speed):     # 생성자 (기본형은 __init__(self):)
        self.name = name
        self.color = color
        self.speed = speed

    def printMyCar(self):
        # (name, color, speed) = (BMW, red, 30)
        print("(name, color, speed) = (", self.name, ", ", self.color, ", ", self.speed, ")")

# bmw = MyCar()   --> 이렇게 쓰면 오류남(위에 생성자가 파라미터가 있는 형태라서)
bmw = MyCar("bmw", "red", 100)
bmw.printMyCar()

class NewCar:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year

    def printNewCar(self):
        print("New Car : (name)", self.name, ", (price)", self.price, ", (year)", self.year)

tesla = NewCar("Tesla", 50000000, 2021)
tesla.printNewCar()

class Bus:
    nation = "KOREA"                    # class 변수
    def __init__(self, name, color):    # 인스턴스 변수 (= 객체마다 갖는 변수)
        self.name = name
        self.color = color

    def printBus(self):
        print("(name, color, nation) = (", self.name, ", ", self.color, ", ", self.nation, ")")

bus1 = Bus("bus1", "red")
bus2 = Bus("bus2", "blue")

bus1.printBus()
bus2.printBus()

bus1.nation = "JAPAN"

bus1.printBus()
bus2.printBus()

print("-" * 80)


class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name

    def addTrick(self, trick):
        self.tricks.append(trick)

puppy = Dog('puppy')
doge = Dog('doge')

puppy.addTrick("roll")
puppy.addTrick("bark")
print(doge.tricks)
doge.addTrick("sleep")
doge.addTrick("eat")
print(puppy.tricks)


class BullDog:
    tricks = []
    def __init__(self, name):
        self.name = name
        self.tricks = []    # 인스턴스

    def addTrick(self, trick):
        self.tricks.append(trick)

puppy = BullDog('puppy')
doge = BullDog('doge')

puppy.addTrick("roll")
puppy.addTrick("bark")
doge.addTrick("sleep")
doge.addTrick("eat")

print(doge.tricks)
print(puppy.tricks)
print(Dog.tricks)

print(dir(BullDog))     # dir() : 클래스 내부에 있는 객체 확인

print("-" * 80)

class Truck:
    __nation = "KOREA"                    # __변수 : 변수 장식
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def printTruck(self):
        print("(name, color, nation) = (", self.name, ", ", self.color, ", ", self.__nation, ")") # class 내 읽기 가능

    def setNation(self, nation):        # Setter
        self.__nation = nation

    def getNation(self):                # getter
        return self.__nation

truck = Truck("Truck", "green")
truck.printTruck()
print(truck.name)
# print(truck.__nation)   --> 이렇게 하면 오류남 (__가 Java의 private역할)      # class 외 읽기 불가능
truck.setNation("USA")
truck.printTruck()
print(truck.getNation())

