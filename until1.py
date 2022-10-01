# 어떠한 수 N이 1이 될 때까지
# K : 나누는 수
# count: 전체 과정을 실행한 횟수

# 다음의 두 과정을 선택해서 수행할 수 있다. (단 2번은 N이 K로 나누어떨어질 때에만 선택 가능)
# N에서 1을 뺀다.
# N을 K로 나눈다.

n, k = map(int, input().split());

count = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        count += 1
    # k로 나누기
    n //= k
    count += 1

#마지막으로 남은 수에 대해 1씩 빼기
while n > 1:
    n -= 1
    count += 1

print(count)