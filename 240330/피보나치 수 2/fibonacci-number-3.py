def fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        # 1,000,000,007로 나눈 게 시간 초과를 방지하는 목적
        a, b = b, (a + b) % 1000000007

    return b

n = int(input())
print(fibonacci(n))