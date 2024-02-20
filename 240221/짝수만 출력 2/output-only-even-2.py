b, a = map(int, input().split())

if b % 2 != 0:
    b = b - 1

while b >= a:
    print(b, end=' ')
    b -= 2