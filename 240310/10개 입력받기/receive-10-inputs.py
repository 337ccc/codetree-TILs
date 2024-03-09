arr = list(map(int, input().split()))

total = 0
count = 0
for i in range(10):
    if arr[i] != 0:
        total += arr[i]
        count += 1
    else:
        break

print(total, f'{total / count:.1f}')