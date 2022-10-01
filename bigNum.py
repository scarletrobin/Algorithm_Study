
# 배열의 크기: N
# 총 더해지는 횟수: M
# 연속 가능 횟수: K

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수를 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수
print("정렬된 데이터: ", data)
print("가장 큰 수 : ", first)
print("두 번째로 큰 수 : ", second)
result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print("result: ", result)

# 생각해보기: M의 크기가 100억 이상처럼 커진다면? 더 효율적으로 푸는 방식을 생각해보아야 한다.