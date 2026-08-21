# function :  여러 개의 수행문을 하나의 이름으로 묶은 실행 단위
# 함수 공유의 공간을 갖는다.
# 자원의 재활용이 가능
# ...

# 내장함수 : 일부 체험
print(sum([1,2,3]))
print(8, bin(8)) 
print(eval('4 + 5'))
print(round(1.2), round(1.6))
import math
print(math.ceil(1.2), ' ', math.ceil(1.6)) # 올림
print(math.floor(1.2), ' ', math.floor(1.6)) # 내림

b_list = [True, 1, False]
print(all(b_list)) # False
print(any(b_list)) # True

data1 = [10, 20, 30]
data2 = ['a', 'b']
for i in zip(data1, data2):
    print(i)
# (10, 'a')
# (20, 'b')

# ... # 업무 특성상 내장함수 지원 안될 수 도있음

import builtins # 자동 로딩
builtins.print("자동 로딩") # builtins
builtins.print(builtins.sum([2,5]))
# print = 7
# print("안녕") 
# 함수(Function) → 모듈(Module) → 클래스(Class)
# 함수 = 특정 작업을 하는 기능
# 모듈 = 여러 기능을 모아놓은 파일
# 클래스 = 데이터와 기능을 하나로 묶어 객체를 만드는 설계도
# 클래스 안의 함수 = 메서드(Method)