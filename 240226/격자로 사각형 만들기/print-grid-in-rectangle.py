n = int(input())

# arr = [[1] * n] + [[1]] * (n - 1)라고 작성하면 안 됨
# deep copy가 아닌 메모리를 공유하는 shallow copy가 진행되기 때문
arr = [[1] * n] + [[1] for _ in range(n - 1)]

for i in range(1, n):
    for j in range(1, n):
        num = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i][j - 1]
        arr[i].append(num)

for m in range(n):
    print(*arr[m])