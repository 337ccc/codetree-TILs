arr = list(input())

total = 10

for i in range(1, len(arr)):
    if arr[i - 1] == arr[i]:
        total += 5
    else:
        total += 10

print(total)