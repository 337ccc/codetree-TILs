A, B = map(float, input().split())

if A > B:
    big = A
    small = B
else:
    big = B
    small = A

count = 0

for i in range(1, 32):
    if small < i ** 2 < big:
        count += 1

print(count)