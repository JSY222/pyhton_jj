print('문4) 추상 클래스')

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def data_print(self):
        pass

    def irumnai_print(self):
        print(f"이름 : {self.irum} , 나이 : {self.nai}", end = " , ")


class Temporary(Employee):
    def __init__(self, irum, nai, ilsu, ildang):
        super().__init__(irum, nai)
        # Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang

    def pay(self):
        return self.ilsu * self.ildang

    def data_print(self):
        self.irumnai_print()
        print(f"월급 : {self.pay()}")


class Regular(Employee):
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = salary

    def pay(self):
        return self.salary

    def data_print(self):
        self.irumnai_print()
        print(f"급여 : {self.pay()}")


class Salesman(Employee):
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai)
        self.salary = salary
        self.sales = sales
        self.commission = commission

    def pay(self):
        return self.salary + self.sales * self.commission

    def data_print(self):
        self.irumnai_print()
        print(f"수령액 : {round(self.pay())}")


t = Temporary("홍길동", 25, 20, 15000)
r = Regular("한국인", 27, 3500000)
s = Salesman("손오공", 29, 1200000, 5000000, 0.25)

t.data_print()
r.data_print()
s.data_print()

print()

class Bicycle:
    def __init__(self, name, wheel, price):
        self.name = name
        self.wheel = wheel
        self.price = price

    def display(self):
        retotal_price = self.wheel * self.price
        print(f"{self.name}님 자전거 바퀴 가격 총액은 {total_price}원 입니다")

gildong = Bicycle('길동', 2, 50000)
gildong.display()