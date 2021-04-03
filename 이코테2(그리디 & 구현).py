# 그리디 알고리즘 : 현재 상황에서 지금 당장 가장 좋은 것만 고르는 방법 (탐욕법), 최소한의 아이디어

# 거스름 돈 문제

n = 1260
count = 0 
array = [500, 100, 50, 10] # 큰 단위의 화폐부터 차례대로 확인

for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count) # 6

# 1이 될 때까지 문제

N = 17
K = 4
cnt = 0

while N != 1:
    if N % K == 0:
        N = N / K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt) # 3

# 곱하기 혹은 더하기 문제

data = input()
result = int(data[0])

for i in range(1, len(data)):
    if int(data[i]) <= 1 or result <= 1:
        result += int(data[i])
    else:
        result *= int(data[i])

print(result)

N = input()
X = list(map(int, input().split()))
X.sort()
result = 0 # 총 그룹의 수
cnt = 0 # 현재 그룹에 포함된 모험가의 수

for i in X: # 공포도 낮은 순으로 확인
    cnt += 1 # 현재 그룹에 해당 모험가 포함
    if cnt >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가
        cnt = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)



# 구현 : 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭, 출력 형태의 변경 등

# 행렬

for i in range(5):
    for j in range(5):
        print('(', i, ',', j, ')', end=' ')
    print()
'''( 0 , 0 ) ( 0 , 1 ) ( 0 , 2 ) ( 0 , 3 ) ( 0 , 4 )
   ( 1 , 0 ) ( 1 , 1 ) ( 1 , 2 ) ( 1 , 3 ) ( 1 , 4 )
   ( 2 , 0 ) ( 2 , 1 ) ( 2 , 2 ) ( 2 , 3 ) ( 2 , 4 )
   ( 3 , 0 ) ( 3 , 1 ) ( 3 , 2 ) ( 3 , 3 ) ( 3 , 4 )
   ( 4 , 0 ) ( 4 , 1 ) ( 4 , 2 ) ( 4 , 3 ) ( 4 , 4 )'''

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 현재
x, y = 2, 2
for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
'''2 3
   1 2
   2 1
   3 2'''

# 상하좌우 문제

x, y = 1, 1
N = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans: # 이동 계획을 확인
    for i in range(len(move)): # 이동 후 좌표 구하기
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N: # 공간을 벗어나는 경우
        continue
    x, y = nx, ny

print(x, y) # 3 4

# 시각 문제 : 완전 탐색 유형

N = 15
cnt = 0

for i in range(15):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt) # 27675

# 왕실의 나이트 문제

n = 'c2'
row = int(n[1]) # 2
column = int(ord(n[0])) - int(ord('a')) + 1 # 3

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 나이트가 이동할 수 있는 경우의 수

cnt = 0
for step in steps: # 이동하고자 하는 위치 확인
    n_row = row + step[0]
    n_column = column + step[1]
    if n_row >= 1 and n_row <= 8 and n_column >= 1 and n_column <= 8: # 해당 위치로 이동 가능할 시 카운트 증가
        cnt += 1

print(cnt) # 6

# 문자열 재정렬 문제

n = 'K1KA5CB7'
cnt = 0
result = []

for i in n: # 문자를 하나씩 확인
    if i.isalpha(): # 알피벳인지 확인
        result.append(i)
    else:
        cnt += int(i)

result.sort() # 알파벳 오름차순

if cnt != 0:
    result.append(str(cnt)) # 숫자가 하나라도 존재할 경우 가장 뒤에 삽입

print(''.join(result)) # .join : 리스트를 문자열로 변환하여 출력 = ABCKK13