# 다이나믹 프로그래밍 : 메모리를 적절하게 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법, 이미 계산한 결과를 별도의 메모리에 저장하여 다시 계산 안하게 함

# 사용 경우 : 최적 부분 구조, 중복되는 부분 문제

# 피보자치 수열 : 점화식(인접한 항들 사이의 관계식)을 활용, 1/1/2/3/4/8/13/21/34...

def fibo(x): # 단순 재귀함수로 구현 : 시간복잡도 큼
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4)) # 3



# 메모이제이션 : 한 번 계산한 결과를 메모리 공간에 메모, 캐싱, 시간복잡도를 줄일 수 있음

# 탑다운(메모이제이션) vs 보텀업(다이나믹 프로그래밍의 전형적인 형태)

# 피보나치 수열을 탑다운 다이나믹 프로그래밍으로 구현

d = [0] * 100 # 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

def fibo(x): # 피보나치 함수를 재귀 함수로 구현(탑다운 다이나믹 프로그래밍)
    if x == 1 or x == 2: # 종료조건
        return 1
    if d[x] != 0: # 이미 계산한 적이 있는 문제라면 그대로 반환
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2) # 아직 계산하지 않았다면 점화식에 따라서 피보나치 결과 반환
    return d[x]

print(fibo(99)) # 218922995834555169026

# 피보나치 수열을 보텀업 다이나믹 프로그래밍으로 구현

d = [0] * 100

d[1] = 1 # 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[2] = 1
n = 99

for i in range(3, n + 1): # 피보나치 함수 반복문으로 구현(보텀업 다이나믹 프로그래밍)
    d[i] = d[i - 1] + d[i - 2]

print(d[n]) # 218922995834555169026



# 개미전사 예제

n = int(input()) # 정수 N을 입력 받기
array = list(map(int, input().split())) # 모든 식량 정보 입력 받기

d = [0] * 100 # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화

d[0] = array[0] # 다이나믹 프로그래밍 진행 (보텀업)
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n -1]) # 계산된 결과 출력



# 1로 만들기 예제

x = int(input()) # 정수 X를 입력 받기

d = [0] * 30001 # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화

for i in range(2, x + 1): # 다이나믹 프로그래밍 진행 (보텀업)
    d[i] = d[i - 1] + 1 # 현재의 수에서 1을 빼는 경우
    if i % 2 == 0: # 현재의 수가 2로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0: # 현재의 수가 3으로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0: # 현재의 수가 5로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])



# 효율적인 화폐 구성 예제

n, m = map(int, input().split()) # 정수 N, M을 입력 받기

array = [] # N개의 화폐단위 정보를 입력받기
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1) # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화 (10001은 무한대 값을 의미)

d[0] = 0 # 다이나믹 프로그래밍 진행 (보텀업)
for i in range(n): # i는 각각의 화폐 단위
    for j in range(array[i], m + 1): # j는 각각의 금액
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우

if d[m] = 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])



# 금광 예제

for tc in range(int(input())): # 테스트 케이스 입력
    n, m = map(int, input().split()) # 금광 정보 입력
    array = list(map(int, input().split()))
    dp = [] # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    index = 0
    
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    
    for j in range(1, m): # 다이나믹 프로그래밍 진행
        for i in range(n):
            if i == 0: left_up = 0 # 왼쪽 위에서 오는 경우
            else: left_up = dp[i - 1][j - 1]
            if i == n - 1: left_down = 0 # 왼쪽 아래에서 오는 경우
            else: left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1] # 왼쪽에서 오는 경우
            dp[i][j] = dp[i][j] + max(lesf_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)



# 병사 배치하기 예제

n = int(input())
array = list(map(int, input().split()))

array.reverse() # 순서를 뒤집어 '최장 증가 부분 수열'문제로 전환

dp = [1] * n # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화

for i in range(1, n): # 가장 긴 증가하는 부분 수열 (LIS) 알고리즘 수행
    for j in rangr(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp)) # 열외해야 하는 병사의 최소 수를 출력