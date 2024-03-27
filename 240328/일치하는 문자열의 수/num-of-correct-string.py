n, A = input().split()
n = int(n)

count = 0
for _ in range(n):
    if A == input():
        count += 1

print(count)