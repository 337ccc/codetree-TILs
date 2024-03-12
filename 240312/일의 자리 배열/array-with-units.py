first, second = map(int, input().split())
arr = [first, second]

for i in range(2, 10):
    result = arr[i - 2] + arr[i - 1]
    result %= 10
    arr.append(result)

print(*arr)