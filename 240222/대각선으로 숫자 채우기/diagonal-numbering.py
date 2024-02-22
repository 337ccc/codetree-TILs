n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

num = 1
if n == 1:
    for i in range(1, m + 1):
        print(i, end=' ')
elif m == 1:
    for j in range(1, n + 1):
        print(j)
else:
    for k in range(n + m - 1):
        for l in range(n):
            if l <= k and k - l <= m - 1:
                arr[l][k - l] = num
                num += 1
            else:
                continue

    for line in range(n):
        print(*arr[line])