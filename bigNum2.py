
# 배열의 크기: N
# 총 더해지는 횟수: M
# 연속 가능 횟수: K

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수
print("정렬된 데이터: ", data)
print("가장 큰 수 : ", first)
print("두 번째로 큰 수 : ", second)
print("반복해서 더해지는 수 : ", first * k + second)

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)  # k + 1 로 나누어떨어지지 않는 경우도 고려 : 그 수만큼 큰 수를 추가로 더하게 됨
print("가장 큰 수가 더해지는 횟수 count: ", count)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print("result : ", result)  # 최종 답안 출력
