# 11654	 아스키 코드

print (ord(input())) # 문자 -> 아스키코드 : chr(), 아스키코드 -> 문자 : ord()



# 11720	 숫자의 합

N = int(input()) # N = 5
n = str(input()) # n = 12345
t = 0

for i in range(N): # i = 0
    t += int(n[i]) # 0 + 1
    
print(t)



# 10809	 알파벳 찾기

S = input() # S = apple
alphabet = list(range(ord('a'), ord('z') + 1)) # 아스키코드 숫자 범위 [97, 98, ..., 123]

for i in alphabet: # i = 97
    print(S.find(chr(i)), end=" ") # find : 문자가 문자열 안에 처음으로 위치한 순서, 없을 경우 -1



# 2675	 문자열 반복

T = int(input()) # 2

for i in range(T): 
    R, S = input().split() # 1 abc
    for j in S: # a
        print(j * int(R), end="") # aabbcc
    print() # 줄넘김



# 1157	 단어 공부

w = input().upper() # APPLE
unique_w = list(set(w)) # [A, P, L, E]
cnt_list = []

for i in unique_w: # i = A
    cnt = w.count(i) # cnt = 1
    cnt_list.append(cnt) # cnt_list = [1]
# cnt_list = [1, 2, 1, 1]

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    print(unique_w[cnt_list.index(max(cnt_list))])



# 1152	 단어의 개수

w = input().strip() # 맨앞뒤 공백 제거 (rstrip(), lstrip())

if len(w) == 0: # 공백은 length = 0
    print(0)
else:
    print(w.count(" ") + 1)



# 2908	 상수

a, b = input().split() # 734 893
A = int(a[::-1]) # 437
B = int(b[::-1]) # 398

if A > B:
    print(A)
elif A < B:
    print(B)



# 5622	 다이얼

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS','TUV', 'WXYZ']
N = input() # UNUCIC
ret = 0

for i in range(len(N)): # i = 0 ~ 5
    for j in dial: # j = ABC ~ WXYZ
        if N[i] in j: # U in TUV
            ret += dial.index(j) + 3
        # ret = 6 + 3

print(ret)



# 2941	 크로아티아 알파벳

chg = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = input() # ddz=z=

for i in chg: # i = dz=
    if i in N: # dz= in ddz=z=
        N = N.replace(i, " ") # d" "z=
# d" "" "

print(len(N)) # 3   



# 1316	 그룹 단어 체커

N = int(input()) # 3
group_word = 0

for i in range(N): # i = 0, 1, 2
    word = input() # word = happy
    error = 0
    for index in range(len(word) - 1 ): # index = 0, 1, 2, 3
        if word[index] != word[index + 1]: # h != a
            new_word = word[index + 1:] # appy
            if new_word.count(word[index]) > 0: # appy.count(h) = 0
                error += 1 
    if error == 0:
        group_word += 1

print(group_word)