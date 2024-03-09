arr = list(map(int, input().split()))

count = 0
total = 0
for i in arr:
    if i != 0:
        if i % 2 == 0:
            count += 1
            total += i
    else:
        break

print(count, total)