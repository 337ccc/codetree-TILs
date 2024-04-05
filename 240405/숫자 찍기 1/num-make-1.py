n, type = map(int, input().split())

if type == 1:
    num = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            for j in range(i):
                num += 1
                print(num, end=' ')
        else:
            num = (i * (i + 1)) // 2 + 1
            for j in range(i):
                num -= 1
                print(num, end=' ')
            num = (i * (i + 1)) // 2
        print()

elif type == 2:
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end=' ')
        count = 2 * i - 1
        num = n - i
        num_lst = list(num for _ in range(count))
        print(*num_lst)

elif type == 3:
    for i in range(1, n + 1):
        if i <= (n // 2) + 1:
            for j in range(1, i + 1):
                print(j, end=' ')
        else:
            for j in range(1, (n + 2) - i):
                print(j, end=' ')
        print()