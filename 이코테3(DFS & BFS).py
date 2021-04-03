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
    3. 더 이상 2번 수앵 불가할 때까지 반복 '''

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

# BFS : 너비 우선 탐색, 가까운 노드부터 우선적으로 탐색, 큐 자료구조 이용, 최단거리 문제 활용

''' 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복 '''

# BFS 동작 예시

from collections import deque

def bfs(graph, start, visited): # BFS 함수 정의
    queue = deque([start]) # 큐 구현을 위해 deque 라이브러리 사용
    visited[start] = True # 현재 노드를 방문 처리
    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft() # 큐에서 하나의 원소를 뽑아 출력
        print(v, end=' ')
        for i in graph[v]: # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [ # 각 노드가 연결된 정보를 표현 (2 차원 리스트) 1 = 2 3 8, 2 = 1 7, 3 = 1 4 5 ...
    [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]
]

visited = [False] * 9 # 각 노드가 방문된 정보를 표현 (1 차원 리스트) 1= false, 2 = false, 3 = false ... 의미

bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6



# 음료수 얼려 먹기 예제

def dfs(x, y): # DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
    if x <= -1 or x >= n or y <= -1 or y >= m: # 주어진 범위를 벗어나는 경우에는 즉시 종료
        return False
    if graph[x][y] == 0: # 현재노드를 아직 방문 안했다면
        graph[x][y] = 1 # 해당 노드를 방문 처리
        dfs(x - 1, y) # 상하좌우의 위치들도 모두 재귀적으로 호출
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(s, y + 1)
        return True
    return False

n, m = map(int, input().split()) # n, m 입력 받기

graph = []
for _ in range(n):
    graph.append(list(map(int, input()))) # 2차원 리스트의 맵 정보 받기

result = 0
for i in range(n): # 모든 노드에 대하여 음료수 채우기
    for j in range(m):
        if dfs(i, j) == True: # 현재 위치에서 DFS 수행
            result += 1

print(result)

# 미로 탈출 예제

from collections import deque

def bfs(x, y): # BFS 코드 구현
    queue = deque()
    queue.append((x, y))
    while queue: # 큐가 빌 때까지 반복
        x, y = queue.popleft()
        for i in range(4): # 현재 위치에서 4가지 방향으로의 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 미로 찾기 공간을 벗어난 경우 무시
                continue
            if graph[nx][ny] == 0: # 벽인 경우 무시
                continue
            if graph[nx][ny] == 1: # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1] # 가장 오른쪽 아래까지의 최단 거리 반환

n, m = map(int, input().split()) # n, m 입력 받기

graph = []
for _ in range(n):
    graph.append(list(map(int, input()))) # 2차원 리스트의 맵 정보 받기

dx = [-1, 1, 0, 0] # 이동할 4가지 방향 정의
dy = [0, 0, -1, 1]

print(bfs(0, 0)) # BFS 실행결과 출력