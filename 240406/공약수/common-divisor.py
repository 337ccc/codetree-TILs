n = int(input())
if n == 2:
    a, b = map(int, input().split())
    num = min(a, b)
    for i in range(1, num + 1):
        if a % i == 0 and b % i == 0:
            print(i)
else:
    a, b, c = map(int, input().split())
    num = min(a, b, c)
    for i in range(1, num + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            print(i)