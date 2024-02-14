n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        num = 7 + 8 * (j // 2)
        if j % 2 == 0:
            arr[i][j] = 4 * j + i
        else:
            arr[i][j] = num - i

for line in arr:
    print(*line)