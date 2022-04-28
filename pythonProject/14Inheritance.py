# 14Inheritance.py

class Car:
    nation = "KOREA"
    def __init__(self, name, color):    # 생성자
        self.name = name
        self.color = color
        print("Car Created...")
    def printCar(self):
        print("(name, color, nation) = (", self.name, ", ", self.color, ", ", self.nation, ")")


class SportsCar(Car):                   # 상속 (Java) class SportsCar extends Car {
    def __init__(self, name, color, turbo = True):   # = True : 따로 값이 없으면 디폴트로 트루를 넣겠다.
        super().__init__(name, color)   # 부모Class가 디폴트생성자가 없어서, 상속Class에서 알아서 불러오지 못함
        self.turbo = turbo              # name, color은 부모Class 따르고, turbo는 상속Class에서 세팅하겠다.
        print("SportsCar Created...")
    def printCar(self):
        print("(name, color, nation, turbo) = (", self.name, ", ", self.color, ", ", self.nation, ", ", self.turbo, ")")

bmw = SportsCar("BMW", "red")           # turbo 안써도 자동으로 true됨
bmw.printCar()