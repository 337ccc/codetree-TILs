n = int(input())

arr = [[0] * n for _ in range(n)]
if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:  # 홀수 열
                arr[j][i] = n * (n - i - 1) + 1 + j
            else:  # 짝수 열
                arr[j][i] = n * (n - i) - j
else:
    for k in range(n):
        for l in range(n):
            if k % 2 == 0:
                arr[l][k] = n * (n - k) - l
            else:
                arr[l][k] = n * (n - k - 1) + l + 1

for line in range(n):
    print(*arr[line])