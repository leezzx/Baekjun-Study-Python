# 2739	 구구단

N = int(input())

for n in range(1,10):
    print(N, '*', n, '=', N * n)



# 10950	 A+B - 3

T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    print(A + B)



# 8393	 합

n = int(input())
t = 0

for N in range(n + 1):
    t += N
print(t)



# 15552	 빠른 A+B

import sys

T = int(sys.stdin.readline())

for t in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)



# 2741	 N 찍기

N = int(input())

for n in range(1, (N + 1)):
    print(n)



# 2742	 기찍 N

N = int(input())

for n in range(N):
    print(N - n)



# 11021	 A+B - 7

T = int(input())

for x in range(1, (T + 1)):
    A, B = map(int, input().split())
    print(f'Case #{x}: {A} + {B} = {A + B}')



# 11022	 A+B - 8

T = int(input())

for x in range(1, (T + 1)):
    A, B = map(int, input().split())
    print('Case #{0}: {1}'.format(x, A + B))



# 2438	 별 찍기 - 1

N = int(input())

for n in range(1, (N + 1)):
    print('*' * n)



# 2439	 별 찍기 - 2

N = int(input())

for n in range(1, (N + 1)):
    print(' ' * (N - n) + '*' * n)



# 10871	 X보다 작은 수

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")