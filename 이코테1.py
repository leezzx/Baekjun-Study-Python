# 리스트 컴프리헨션

array = [i for i in range(10) if i % 2 == 1]
print(array) # [1, 3, 5, 7, 9]



# 아무것도 처리하고 싶지 않을 때 : pass (나중에 입력하기 위해 남겨둠)



# 조건문의 간소화 : 실행될 소스코드가 한 줄인 경우, 줄 바꿈 안해도 됨

score = 85
if score >= 80: result = "Sucecss"
else: result = "Fail" 
print(result) # Success

# 조건부 표현식은 if문을 한 줄에 작성할 수 있음

score = 85
result = "Success" if score >= 80 else "Fail"
print(result) # Success



# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 : continue

result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i
print(result) # 25

# 반복문 즉시 탈출 : break

i = 1
while True:
    print(i) # 1 2 3 4 5
    if i == 5:
        break
    i += 1



# 함수 내에서 전역변수 참조 : global

a = 0
def func():
    global a
    a += 1
for _ in range(10):
    func()
print(a) # 10

# 파이썬에서 함수는 여러 값 반환 가능

def operator(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = round(a / b, 3)
    return add, subtract, multiply, divide
a, b, c, d = operator(7, 3)
print(a, b, c, d) # 10 4 21 2.333

# 람다 표현식을 이용하여 함수를 한줄에 작성 가능

print((lambda a, b: a + b)(3, 7)) # 10

array = [('홍', 50), ('이', 32), ('김', 74)]
print(sorted(array, key=lambda x: x[1])) # sorted with key, [('이', 32), ('홍', 50), ('김', 74)]



# 내징함수

# eval()
result = eval("(3 + 5) * 7")
print(result) # 56

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result) # [1, 4, 5, 8, 9]
print(reverse_result) # [9, 8, 5, 4, 1]



# 순열 : 서로 다른 n개에서 서로 다른 r개를 일렬로 나열 abc, acb, bac, bca, cab, cba

from itertools import permutations
data = ['a', 'b', 'c']
result = list(permutations(data, 3))
print(result) # [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

# 조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 ab, ac, bc

from itertools import combinations
data = ['a', 'b', 'c']
result = list(combinations(data, 2))
print(result) # [('a', 'b'), ('a', 'c'), ('b', 'c')]

# Counter : 등장 횟수를 세는 기능

from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # 3
print(counter['red']) # 2
print(dict(counter)) # {'red': 2, 'blue': 3, 'green': 1}

# gcd() : 최대 공약수

import math
def lcm(a, b): # 최소 공배수 구하는 함수 만들기
    return a * b // math.gcd(a, b)
print((lambda a, b: math.gcd(a, b))(21, 14)) # 7
print(lcm(21, 14)) # 42