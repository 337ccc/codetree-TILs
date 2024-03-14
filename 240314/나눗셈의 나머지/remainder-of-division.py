a, b = map(int, input().split())
arr = [0 for _ in range(b)]

while a > 1:
    remainder = a % b
    arr[remainder - 1] += 1
    a //= b

total = 0
for i in arr:
    total += i ** 2

print(total)