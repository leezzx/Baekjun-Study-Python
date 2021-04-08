# 정렬(shorting) : 데이터를 특정한 기준에 따라 순서대로 나열하는 것

# 선택 정렬 : 가장 작은 데이터를 선택하여 맨 앞에 있는 데이터와 바꾸는 것을 반복

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# 삽입 정렬 : 적절한 위치에 값을 삽입, 선택 정렬보다 어렵지만 더 효율적

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j] # 스와프
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# 퀵 정렬 : 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법, 가장 많이 사용되는 정렬 알고리즘, 보통 첫 번째 데이터를 기준데이터(Pivot)로 설정

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]): # 피벗보다 큰 데이터를 찾을 때까지 반복
            left += 1
        while(right > start and array[right] >= array[pivot]): # 피벗보다 작은 데이터를 찾을 때까지 반복
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 더 간단하게

def quick_sort1(array):
    if len(array) <= 1: # 리스트가 하나 이하의 원소만을 담고 있다면 종료
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 원소 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort1(left_side) + [pivot] + quick_sort1(right_side) # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환

print(quick_sort1(array)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# 계수 정렬 : 특정 조건에서 매우 빠르게 동작하는 정렬 알고리즘, 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용가능

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1) # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=" ") # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

# 두 배열의 원소 교체 예체

n, k = map(int, input().split()) # n, k 입력 받기
a = list(map(int, input().split())) # 배열 a의 원소 입력 받기
b = list(map(int, input().split())) # 배열 b의 원소 입력 받기

a.sort() # a를 오름차순으로 정렬
b.sort(reverse = True) # b를 내림차순으로 정렬

for i in range(k):
    if a[i] > b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))