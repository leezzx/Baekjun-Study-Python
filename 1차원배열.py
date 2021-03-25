# 10818	 최소, 최대

N = int(input())
i = list(map(int, input().split()))

print('{} {}'.format(min(i), max(i)))



# 2562	 최댓값

num_list = []

for numbers in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list)) + 1)



# 2577	 숫자의 개수

i = 1

for numbers in range(3):
    n = int(input())
    i *= n
    
i_str = str(i) # 각 자리의 숫자를 분리하기 위해 문자열 형식으로 저장

for num in range(10):
    print(i_str.count(str(num)))



# 3052	 나머지

n = set()

for nubers in range(10):
    i = int(input())
    n.add(i % 42)
    
print(len(n))



# 1546	 평균

n = int(input()) # 3
score = list(map(float, input().split())) # 소수점 출력을 위한 float = 40, 80, 60
max = 0

for i in range(n): # i = 0
    if max < score[i]: # 0 < 40
        max = score[i] # max = 40
# max = 60

for i in range(n): # i = 0
    score[i] = (score[i] / max) * 100 # score[0] = (40 / 60) * 100
    
sum = 0
for i in range(n):
    sum += score[i]
    
print(sum / n)



# 8958	 OX퀴즈

n = int(input())

for i in range(n):
    ox_list = str(input())
    score = 0
    sum_score = 0 # 새로운 ox 리스트 입력 받아 점수 합계를 리셋
    for ox in list(ox_list):
        if ox == 'O':
            score += 1 # 'O'가 연속되면 점수가 1점씩 증가
            sum_score += score
        elif ox == 'X':
            score = 0
    print(sum_score)



# 4344	 평균은 넘겠지

C = int(input())

for i in range(C):
    N_list = list(map(int, input().split()))
    avg = sum(N_list[1:]) / N_list[0]
    cnt = 0
    for j in N_list[1:]:
        if j > avg:
            cnt += 1
    print(str("%.3f" % round((cnt / N_list[0]) * 100, 3)) + "%")