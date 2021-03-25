# 10952	 A+B - 5

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)



# 10951	 A+B - 4

a,b=(0,0)

while 1:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break 



# 1110	 더하기 사이클

N = int(input()) # 26
num = N # num = 26
i = 0

while True:
    sum_num = (num // 10) + (num % 10) # sum_num = 2 + 6 = 8
    new_num = ((num % 10) * 10) + (sum_num % 10) # new_num = 60 + 8 = 68
    i += 1
    if new_num == N: # 26 == 26
        break
    num = new_num # num = 68

print(i)