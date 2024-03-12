n = int(input())

arr = [1, n]
order = 1
num = 0
while num <= 100:
    order += 1
    num = arr[order - 2] + arr[order - 1]
    arr.append(num)

print(*arr)