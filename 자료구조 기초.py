# 1. array

size = 3
arr = [0] * size
print(arr) # [0, 0, 0]

arr = [True] * 5
print(arr) # [True, True, True, True, True]

arr = ['a'] * 5
print(arr) # ['a', 'a', 'a', 'a', 'a']

print(len(arr)) # 5



# 2. list

arr = []
arr2 = [1, 2, 3, 4]
print(arr2) # [1, 2, 3, 4]

arr.append(10)
arr.append(20)
arr.append(30)
print(arr) # [10, 20, 30]

arr.remove(10)
arr.remove(30)
print(arr) # [20]

for i in arr2:
    print(i)
    """1
       2
       3   
       4"""

for i, j in enumerate(arr2): # 인덱스와 값을 모두 출력
    print(i, j) 
    '''0 1
       1 2
       2 3
       3 4'''

print(len(arr2)) # 4



# 3. hash set

s = set()

s.add(10)
s.add(20)
s.add(30)
print(s) # {10, 20, 30}

s.remove(20)
print(s) # {10, 30}

for i in s:
    print(i)
    '''10
       20'''

print(10 in s) # True
print(30 in s) # True
print(40 in s) # False

print(len(s)) # 2



# 4. hash map
m = dict()
m['a'] = 100
m['b'] = 200
print(m) # {'a': 100, 'b': 200}

print(m.get('a')) # 100
print(m.get('c')) # None, print(m['c']) = 에러발생
print(m['b']) # 200

print('a' in m) # True
print('c' in m) # False

for i in m: # = for i in m.keys():
    print(i) # key 값을 출력
    '''a
       b'''

for i in m.values(): # value 출력
    print(i)
    '''100
       200'''

for i, j in m.items(): # 둘다 출력
    print(i, j)
    '''a 100
       b 200'''

print(len(m)) # 2



# 5. stack (fifo : first in first out)

s = [] # stack와 유사

s.append(10)
s.append(20)
s.append(30) # append는 stack에 push하는 것과 유사

while s:
    print(s.pop()) # filo
    '''30
       20
       10'''

# stack 구현

class Stack:
    def __init__ (self):
        self.items = [] # 리스트를 이용하여 stack 생성

    def pop(self): # pop 기능 구현 : 맨 위의 값을 제거
        Stack_length = len(self.items)
        
        if stack_length < 1:
            return "Stack is empty" # Stack이 비어있을 경우 에러메시지 출력

        result = self.items[Stack_length - 1]
        del self.items[Stack_length - 1]
        return result # 가장 위에 있는 item을 반환하며 삭제

    def push(self, x): # push기능 구현 : 맨 위에 값을 추가
        self.items.append(x)

    def peek(self): # Stack의 변형 없이 맨 마지막 값을 출력
        return self.items[-1]

    def isEmpty(self): # 비어있는지 여부를 확인
        return not self.items    