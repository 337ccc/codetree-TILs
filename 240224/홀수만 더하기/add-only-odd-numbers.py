n = int(input())

total = 0
for _ in range(n):
    num = int(input())
    if num % 2 != 0 and num % 3 == 0:
        total += num

print(total)