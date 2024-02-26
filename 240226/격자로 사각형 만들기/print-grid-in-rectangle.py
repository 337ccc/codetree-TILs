n = int(input())
arr = [[1] * n] + [[1] for _ in range(n - 1)]
for i in range(1, n):
    for j in range(1, n):
        num = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i][j - 1]
        arr[i].append(num)

for m in range(n):
    print(*arr[m])