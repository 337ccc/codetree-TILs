a, b = map(int, input().split())
if a >= b:
    big = a
    small = b
else:
    big = b
    small = a

total = 0
for i in range(small, big + 1):
    if i % 5 == 0:
        total += i

print(total)