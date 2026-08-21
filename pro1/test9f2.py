# 사용자 정의 함수
"""
def 함수명(가인수,,,):  # dummy argument, 매개변수
    # ...
    return 반환 값  # 1개만 반환, return이 없으면 return None

함수명(실인수...)   # 함수 호출 # actual argument
"""
print('뭔가를 실행 ...')

# 함수 선언
def doFucn1():
    print('doFucn1 수행')
    return None  # 생략 가능

def doFucn2(name):
    print('name : ', name)

def doFucn3(arg1, arg2): # pass를 쓰면 아무짓도 안하는거
    res = arg1 + arg2
    return res

def doFucn4(a1, a2):
    imsi = a1 + a2
    if imsi % 2 == 1:
        return       # 함수 내에 return은 함수의 무조건 탈출
    else:
        return imsi

    # kbs =9 죽은 문장(안 쓰기)

# 함수 홀출
doFucn1()
print('어떤 자업 처리')
doFucn1()                     # 함수를 실행 가능
print('함수 주소는 ', doFucn1) # <function doFucn1 at 0x00000244EE59F7F0> 16진수로 표현, 주소를 표현
print('함수 주소는 ', id(doFucn1)) # ucn1 at 0x00000244EE59F7F0> 10진수로 표현
imsi = doFucn1                # 함수의 주소를 치환
imsi()                        # 함수를 실행 가능
imsi2 = doFucn1()             # 함수 실행 결과
print(imsi2)                  # 실행 결과를 출력
print(doFucn1())

print('--------')
# dofucn2()  # TypeError : doFucn2() missing 1 required positior
doFucn2(7)
doFucn2("홍길동")

print('--------')
doFucn3("대한", "민국")
print(doFucn3("대한", "민국"))
print(doFucn3(3, 4))
# print(doFucn3(3, "사")) # TypeError
result = doFucn3("3", "4")
print('result : ', result)

print('--------')
print(doFucn4(3, 4))  # None
print(doFucn4(3, 5))  # 8  

print('**' * 30)
def triArea(a, b):
    c = a * b / 2
    triAreaPrint(c)  # 함수 내에서 다른 함수 호출

def triAreaPrint(arg):
    print('삼각형의 면적은 ', arg)

triArea(20, 30)

print()
def passResult(kor, eng):
    ss = kor + eng
    if ss >= 50:
        return True
    else:
        return False
if passResult(20, 10):
    print('합격')
else:
    print('불합격')


print()
def swapFunc(a, b):
    return b, a   # retrun (b, a) # 반환값은 반드시 1개

a = 10; b = 20
print(a, ' ', b)
print(swapFunc(a, b))

print()                           # 이거 전체가 모듈임
def funcTest():
    print('funcTest 멤버 처리')
    def funcInner():
        print('내부함수 funcInner 실행')

    funcInner()

funcTest()

print()
# if 조건식 안에 함수 적용
def isOdd(para):
    return para % 2 == 1 # 홀수이면 True 변환

mydict = {x:x for x in range(11) if isOdd(x)}
print(mydict)

print('\n변수의 생존 범위 (scope rule)')
# 변수가 저장되는 이름공간은 변수가 어디에서 선언 되었는가에 따라 생존 시간이 다르다.
# 전역, 지역 변수
# local > Enclosing function > Global > Built-in
player = '전국대표'  # 전역변수 (현재 파일(모듈) 어디서든 호출 가능)
name = '신기해' # 전역변수

def funcSoccer():  # 프로그램 짤때 이름을 다르게 주기
    name = '이기자' # 지역변수 (현재 함수 내에서만 유효)
    city = '서울'
    print(f'이름은 {name} 수준은 {player}')
    print(f'지역은 {city}')

funcSoccer()
print(f'이름은 {name} 수준은 {player}')
# print(f'지역은 {city}') # NameError: name 'city' is not defined

print()
a = 10; b= 20; c = 30  # 전역변수
print(f"far 수행 전 a:{a}, b:{b}, c:{c}")

def foo():
    a = 7 # 지역변수, 비권장(가독성 떨어짐)
    b = 100

    def bar():
        global c # bar의 멤버가 아니라 모듈의 멤버가 됨(전역)
        nonlocal b
        b = 8 # 지역변수
        print(f"bar 수행 중 a:{a}, b:{b}, c:{c}")
        c = 9 # 지역변수, 선언을 하기전에 C를 찍어서 에러남, 그래서 global c를 줌
        # b = 200 # bar 수준 지역변수
        b = 200 # foo 수준 지역변수, 그래서 nonlocal b를 줌

    bar()
    print(f"bar 수행 후 a:{a}, b:{b}, c:{c}")

foo()
print(f"foo 수행 후 a:{a}, b:{b}, c:{c}")

print() # 시험볼때 잘나옴
g = 1   
print('g : ', g)  # 1
def func():
    global g
    a = g 
    g = 2 # g = 2가 있어 문제됨, 지우던지 global g를 줌
    return a

print(func())
print('g : ', g) # 2

print('작업 종료')   