# 순차탐색 : 데이터를 찾기 위해 앞에서 부터 데이터를 하나식 확인

# 이진탐색 : 탐색 범위를 절반씩 좁혀가며 데이터를 탐색, 시작/끝/중간을 이용하여 탐색 범위 설정

def binary_search(array, target, start, end): # 재귀함수로 구현
    if start > end:
        return None
    mid = (start + end) // 2 # 중간값 설정
    if array[mid] == target: # 찾은 경우 중간값 인덱스 반환
        return mid
    elif array[mid] > target: # 중간값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        return binary_search(array, target, start, mid - 1)
    else: # 중간값 보다 찾고자 하는 값이 큰 경우 오른쪽 값을 확인
        return binary_search(array, target, mid + 1, end)  

n, target = list(map(int, input().split())) # n(원소의 개수)와 target(찾고자 하는 값)을 입력 받기
array = list(map(int, input().split())) # 전체 원소 입력 받기

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

def binary_search2(array, target, start, end): # 반복문으로 구현
    while start <= end:
        mid = (start + end) // 2 # 중간값 설정
        if array[mid] == target: # 찾은 경우 중간값 인덱스 반환
            return mid
        elif array[mid] > target: # 중간값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            end = mid - 1
        else: # 중간값 보다 찾고자 하는 값이 큰 경우 오른쪽 값을 확인
            start = mid + 1
    return None 

n, target = list(map(int, input().split())) # n(원소의 개수)와 target(찾고자 하는 값)을 입력 받기
array = list(map(int, input().split())) # 전체 원소 입력 받기

result = binary_search2(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)



# 파이썬 이진탐색 라이브러리

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환 = 2
print(bisect_right(a, x)) # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환 = 4

# 값이 특정 범위에 속하는 데이터 개수 구하기

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value): # 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9] # 배열 선언

print(count_by_range(a, 4, 4)) # 값이 4인 데이터 개수 출력 = 2
print(count_by_range(a, -1, 3)) # 값이 [-1, 3] 범위에 있는 데이터 개수 출력 = 6



# 파라메트릭 서치 : 최적화 문제를 결정 문제('예'혹은 '아니오')로 바꾸어 해결하는 문제, 이진 탐색 활용



# 떡볶이 떡 만들기 예제 

n, m = list(map(int, input().split())) # n(떡 개수), m(요청한 떡의 길이) 입력 받음
array = list(map(int, input().split())) # 각 떡의 개별 높이 정보를 입력 받음

start = 0
end = max(array)

result = 0 # 이진 탐색 수행 (반복문)
while start <= end:
    total = 0
    mid = (start + end) // 2 # 중간값 설정
    for x in array:
        if x > m: # 잘랐을 때의 떡의 양 계산
            total += x - mid
    if total < m: # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        end = mid - 1
    else: # 떡의 양이 많을 경우 덜 자르기 (오른쪽 부분 탐색)
        result = mid # 최대한 덜 잘랐을 때가 정답임으로, 여기에서 result 기록
        start = mid + 1

print(result)