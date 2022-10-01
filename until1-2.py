# 어떠한 수 N이 1이 될 때까지
# K : 나누는 수
# count: 전체 과정을 실행한 횟수

# 다음의 두 과정을 선택해서 수행할 수 있다. (단 2번은 N이 K로 나누어떨어질 때에만 선택 가능)
# N에서 1을 뺀다.
# N을 K로 나눈다.

# 효율적인 방식: N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 소스코드 작성
n, k = map(int, input().split());

count = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    print("target", target)
    count += (n - target)
    print("count", count)
    n = target
    # n이 K보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K 로 나누기
    count += 1
    n //= k

# 마지막으로 남은 수에 대해 1씩 빼기
count += (n - 1)
print("final count : ", count)
