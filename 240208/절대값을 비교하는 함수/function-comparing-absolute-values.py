n = int(input())

for _ in range(n):
    left, right = map(int, input().split())
    left, right = abs(left), abs(right)
    if left >= right:
        print(left)
    else:
        print(right)