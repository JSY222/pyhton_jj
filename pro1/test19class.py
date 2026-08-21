# oop : 객체지향(중심)적인 프로그래밍 가능. 상속, 포함, 다형성 등의 기법 구사 가능
# calss : 멤버변수(필드), 멤버 메소드로 구성
# 인스턴스에 의해 새로운 이름공간을 갖는다.

import math

a = 2
print(a)

def func():
    print('ok')

class TestClass: # Class의 이름만큼은 대문자로 주기
    aa = 1  # 멤버 변수

    def __init__(self): # 특별 메소드, Method의 첫 인자는 반드시 self
        print('생성자 : 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당')

    def __del__(self):  # 특별 메소드
        print('소멸자 : 프로그램 종료시 자동실행, 마무리 작업')

    def showMessage(self): # 일반 메소드
        name = '한국인'  # 지역변수 : showMessage에서만 유효
        print(name)
        print(self.aa)

print(TestClass)  # <class '__main__.TestClass'>
print('클래스 멤버 a : ', TestClass.aa) # 클래스 멤버  a : 1
# TestClass.showMessage() # TypeError: ...

print()
# 클래스 생성자를 이용해 객체 생성 후 해당 개체의 주소를 객체변수에 치환
test = TestClass() # 생성자 호출, instance을 함, -> object(객체,개체)이 생성 됨
print('클래스 멤버 a : ', test.aa) # test의 주소를 self가 가짐 test.showMessage(test) 들어갔다는 의미
print()
# 1. Bound Method call
test.showMessage() # 자동으로 객체변수 test가 메소드의 인수로 담겨 호출됨

# 2. UnBound Method call : 이미 어디서 만든 객체 변수를 직접 넣어주면 성립됨
TestClass.showMessage(test)

print()
print(type(1))  # <calss 'int'>
print(type(1.0))
print(type('ok'))
print(type(test)) # <class '__main__.TestClass'>

print(id(test))  # 2139952008896
print(id(TestClass)) # 2139954147024
test2 = TestClass() # 객체 한 개 더 생성
print(id(test2))