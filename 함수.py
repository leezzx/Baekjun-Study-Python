# 15596	 정수 N개의 합

def solve(a):
    return sum(a)



# 4673	 셀프 넘버

num = set(range(1, 10001)) # num = (1, 2, ..., 10000)
r_num = set()

for i in range(1, 10001): # i = 860
    for j in str(i): # j = '8', '6', '0'
        i += int(j) # 860 + 8 + 6 + 0 
    r_num.add(i) # 생성자가 있는 숫자
    
s_num = sorted(num - r_num) # sorted : 순서대로 정렬 (list에선 sort())

for k in s_num:
    print(k)



# 1065	 한수

def Hansu(n):
    cnt = 0
    if n < 100: # 입력된 수가 100 미만일 경우 모든 수가 한수 이니 n개의 한수
        return n
    else:
        for i in range(100, (n + 1)): #i = 246
            a = i // 100 # a = 2
            b = (i % 100) // 10 # b = 4
            c = (i % 10) # c = 6
            if (a - b) == (b - c):
                cnt += 1
        return (99 + cnt)

    
num = int(input())
print(Hansu(num))