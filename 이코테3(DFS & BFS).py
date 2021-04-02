# 스텍 자료구조 : 먼저 들어온 데이터가 나중에 나가는 형식의 자료구조, 입구와 출구가 동일한 형태로 스텍을 시각화(프링글스 통)

stack = []
stack.append(5) # [5]
stack.append(2) # [5 2]
stack.append(3) # [5 2 3]
stack.append(7) # [5 2 3 7]
stack.pop() # [5 2 3]
stack.append(1) # [5 2 3 1]
stack.append(4) # [5 2 3 1 4]
stack.pop() # [5 2 3 1]

print(stack[::-1]) # 최 상단 원소부터 출력 = [1, 3, 2, 5]
print(stack) # 최 하단 원소부터 출력 = [5, 2, 3, 1]



# 큐 자료구조 : 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조, 입구와 출구가 모두 뚤려있는 형태로 시각화(터널)

from collections import deque # deque를 통해 시간복잡도를 줄일 수 있음

queue = deque()

queue.append(5) # [5]
queue.append(2) # [5 2]
queue.append(3) # [5 2 3]
queue.append(7) # [5 2 3 7]
queue.popleft() # 가장 왼쪽을 빼기 = [2 3 7]
queue.append(1) # [2 3 7 1]
queue.append(4) # [2 3 7 1 4]
queue.popleft() # [3 7 1 4]

print(queue) # 먼저 들어온 순서대로 출력 = deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 = deque([4, 1, 7, 3])



# 재귀 함수 : 자기자신을 다시 호출하는 함수, 종료 조건을 포함, 스텍과 유사

def recursive_function(i):
    if i == 10:
        return
    print(i, "번째 재귀함수에서", i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)
'''1 번째 재귀함수에서 2 번째 재귀함수를 호출합니다.
   2 번째 재귀함수에서 3 번째 재귀함수를 호출합니다.
   3 번째 재귀함수에서 4 번째 재귀함수를 호출합니다.
   4 번째 재귀함수에서 5 번째 재귀함수를 호출합니다.
   5 번째 재귀함수에서 6 번째 재귀함수를 호출합니다.
   6 번째 재귀함수에서 7 번째 재귀함수를 호출합니다.
   7 번째 재귀함수에서 8 번째 재귀함수를 호출합니다.
   8 번째 재귀함수에서 9 번째 재귀함수를 호출합니다.
   9 번째 재귀함수에서 10 번째 재귀함수를 호출합니다.
   9 번째 재귀함수를 종료합니다.
   8 번째 재귀함수를 종료합니다.
   7 번째 재귀함수를 종료합니다.
   6 번째 재귀함수를 종료합니다.
   5 번째 재귀함수를 종료합니다.
   4 번째 재귀함수를 종료합니다.
   3 번째 재귀함수를 종료합니다.
   2 번째 재귀함수를 종료합니다.
   1 번째 재귀함수를 종료합니다.'''

# n! 예제
   
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1) # n! = n * (n - 1)!

print(factorial_recursive(5)) # 120

# 유클리드 호제법 예제 (최대공약수 계산) : A > B 일때 A를 B로 나눈 나머지 R, A와 B의 최대공약수 = B와 R의 최대공약수

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162)) # 6



# DFS : 깊이 우선 탐색, 스택 자료구조 혹은 재귀함수를 이용함

''' 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄
    3. 더 이상 2번 수앵 불가할 때까지 반복'''

# DFS 소스코드 예제

def dfs(graph, v, visited): # DFS 함수 정의 (재귀함수)
    visited[v] = True # 현재 노드를 방문 처리
    print(v, end=' ')
    for i in graph[v]: # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]: # visited[i] == false 일 때
            dfs(graph, i, visited)

graph = [ # 각 노드가 연결된 정보를 표현 (2 차원 리스트) 1 = 2 3 8, 2 = 1 7, 3 = 1 4 5 ...
    [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]
]

visited = [False] * 9 # 각 노드가 방문된 정보를 표현 (1 차원 리스트) 1= false, 2 = false, 3 = false ... 의미

dfs(graph, 1, visited) # 1 2 7 6 8 3 4 5