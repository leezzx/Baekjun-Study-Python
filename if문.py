# 1330	 두 수 비교하기

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')



# 9498	 시험 성적

a = int(input())

if 90 <= a <= 100:
    print('A')
elif 80 <= a <= 89:
    print('B')
elif 70 <= a <= 79:
    print('C')
elif 60 <= a <= 69:
    print('D')
else:
    print('F')



# 2753	 윤년

a = int(input())

if ((a % 4 == 0) and (a % 100 != 0)) or (a  % 400 == 0):
    print(1)
else:
    print(0)



# 14681	 사분면 고르기

x = int(input())
y = int(input())

if x >= 0 and y >= 0:
    print(1)
elif x <= 0 and y >= 0:
    print(2)
elif x <= 0 and y <= 0:
    print(3)
elif x >= 0 and y <= 0:
    print(4)



# 2884	 알람 시계

h, m = map(int, input().split())

if h > 0:
    if m >= 45:
        print(h, (m - 45))
    else:
        print((h - 1), (m + 15))
elif h == 0:
    if m >= 45:
        print(0, (m - 45))
    else:
        print(23, (m + 15))