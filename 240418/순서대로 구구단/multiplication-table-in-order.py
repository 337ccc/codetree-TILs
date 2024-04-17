a, b = map(int, input().split())

if a <= b:
    for i in range(1, 10):
        for j in range(a, b + 1):
            print(f'{j} * {i} = {j * i}', end='  ')
        print()
else:
    for i in range(1, 10):
        for j in range(b, a - 1, -1):
            print(f'{j} * {i} = {j * i}', end='  ')
        print()