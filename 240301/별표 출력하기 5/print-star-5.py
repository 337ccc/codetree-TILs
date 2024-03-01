n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        factor = ''
        for m in range(i):
            factor += '*'
        print(factor, end=' ')
    print()