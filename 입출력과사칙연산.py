# 2557 Hello World

print('Hello World!')



# 10718	We love kriii

print('강한친구 대한육군\n강한친구 대한육군') # \n으로 엔터역할



# 10171 고양이

print('''\\    /\\''')
print(''' )  ( ')''')
print('''(  /  )''')
print(''' \\(__)|''')



# 10172 개

print('''|\_/|''')
print('''|q p|   /}''')
print('''( 0 )\"\"\"\\''')
print('''|\"^\"`    |''')
print('''||_/=\\\\__|''')



# 1000	 A+B

A, B = input().split() # 입력되는 문자를 input()함수로 입력받고, split()함수로 나누어 A, B에 저장

print(int(A) + int(B)) # int()함수로 A, B를 정수로 변환 뒤 합을 출력



# 1001	 A-B

A, B = input().split()
print(int(A) - int(B))



# 10998	 A×B

A, B = map(int, input().split()) # map함수를 통해 int변환을 먼저함
print(A * B)



# 1008	 A/B

A, B = map(int, input().split())
print(A / B)



# 10869	 사칙연산

A, B = map(int,input().split())
print(A + B)
print(A - B)
print(A * B)
print(int(A / B)) # 나누어떨어지지 않을 때 float형으로 출력됨, 고로 int 처리
print(A % B)



# 10430	 나머지

A, B, C = map(int, input().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)



# 2588	 곱셈

a = int(input())
b = input()
axb2 = a * int(b[2]) # []를 통해 원하는 자리의 문자 가져오기
axb1 = a * int(b[1])
axb0 = a * int(b[0])
axb = a * int(b)
print(axb2, axb1, axb0, axb, sep='\n') # sep : 여러가지 출력할 때 값 사이사이에 들어갈 문자 지정