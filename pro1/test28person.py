# 상속

class Person: # 용도 : 부모 클래스로 사용
    say = '난 사람이야~~~'  # 접근권한 : public
    nai = '20' # class내의 전역변수 
    __msg = 'good : private 멤버 - 현재 클래스에서만 유효'

    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai #
        nai # 메소드에서만 사용가능한 지역변수

    def printInfo(self):  # 접근권한 : public
        print(f'나이:{self.nai}, 이야기:{self.say}')

    def helloMethod(self):
        print('안녕')
        print('hello : ', self.say, self.nai, self.__msg)

print(Person.say, Person.nai)  # 원형 클래스로 멤버 호출 (비권장)
# Person.printTnfo() # TypeError
per = Person('25')  # 객체 변수로 멤버 호출(권장)
per.printInfo()
per.helloMethod()

print('---' * 5)
class Employee(Person):
    subject = '근로자'
    say = '일하는 동물' # hiding(shadowing)

    def __init__(self):
        print('Employee 생성자')

    def printInfo(self): # 메소드 오버라이딩(override) : 내용만 다름
        print('Employee 클래스의 printInfo() 호출된')

    def ePrintInfo(self):
        print(self.subject, self.say, self.nai)
        # print(self.__msg) # 부모 클래스의 private 멤버 호출 : private이니까 안됨, Person클래스만 호출가능, AttributeError
        self.helloMethod()
        self.printInfo() # 현재 클래스에서 먼저 검색 후 없으면 부모 메소드 호출
        super().printInfo() # 현재 클래스가 아니라 바로 부모 메소드 호출
        print(self.say, ',',  super().say) # 일하는 동물, 난 사람이야~~~

emp = Employee()
print(emp.subject, emp.nai, emp.say)
emp.printInfo()
emp.ePrintInfo()

print('---' * 5)
class Worker(Person):
    # def __init__(self, nai):
    #     pass

    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai) # 부모 클래스의 생성자 호출

    def wPrintInfo(self):
        print('Worker - wPrintInfo() 처리')
        self.printInfo()
        super().printInfo() # self.printInfo하고 같다. 최종적으로 만나기때문


wor = Worker('30')
print(wor.say, wor.nai)
wor.wPrintInfo()

print('---' * 5)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        # super(). __init__(nai) # Bound method call
        Worker.__init__(self, nai) # UnBound method call

    def pPrintInfo(self):
        print('Programmer - pPrintInfo() 처리함')

    def wPrintInfo(self):
        print('Programmer 클래스에서 오버라이팅')

pro = Programmer(35)
print(pro.say, pro.nai)
pro.pPrintInfo()
pro.wPrintInfo() 

print('\n클래스 타입 확인 --------')
a = 3; print(type(a)) # <class 'int'> : Maker가 만든 기본 타입
print(type(pro)) # <class '__main__.Programmer'>
print(type(wor)) # <class '__main__.Worker'>

print(Person.__bases__) # (<class 'object'>,) 모든 클래스는 상속받은거임, 슈퍼클래스는 object
print(Employee.__bases__) # (<class '__main__.Person'>,)
print(Worker.__bases__) # (<class '__main__.Person'>,)
print(Programmer.__bases__) # (<class '__main__.Worker'>,)