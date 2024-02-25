n = int(input())

total = 0
count = 0
for _ in range(n):
    num = int(input())
    total += num
    count += 1

print(total, f'{total / count:.1f}')