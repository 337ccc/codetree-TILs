n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        num = n * (j + 1) - 1
        if j % 2 == 0:
            arr[i][j] = n * j + i
        else:
            arr[i][j] = num - i

for line in arr:
    print(*line)