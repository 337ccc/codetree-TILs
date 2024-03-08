start, end = map(int, input().split())

count = 0
for i in range(start, end + 1):
    total = 0
    for j in range(1, i):
        if i % j == 0:
            total += j
    
    if total == i:
        count += 1

print(count)