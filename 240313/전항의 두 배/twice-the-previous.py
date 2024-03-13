num1, num2 = map(int, input().split())

arr = [num1, num2]
for i in range(2, 10):
    new_num = arr[i - 1] + 2 * arr[i - 2]
    arr.append(new_num)

print(*arr)