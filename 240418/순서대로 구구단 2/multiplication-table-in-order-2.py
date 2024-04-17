a, b = map(int, input().split())

if a <= b:
    for i in range(a, b + 1):
        num = 0
        for _ in range(3):
            for j in range(3):
                num += 1
                print(f'{i} * {num} = {i * num}', end='  ')
            print()
        print()
else:
    for i in range(a, b - 1, -1):
        num = 0
        for _ in range(3):
            for j in range(3):
                num += 1
                print(f'{i} * {num} = {i * num}', end='  ')
            print()
        print()