n = int(input())

arr = [[1], [1, 1]]

if n >= 3:
    n = n - 1
    for i in range(1, n):
        line = [1]
        for j in range(1, i + 1):
            num = arr[i][j - 1] + arr[i][j]
            line.append(num)
        line.append(1)
        arr.append(line)

for m in range(n + 1):
    print(*arr[m])