n = int(input())

for i in range(1, 2 * n + 1):
    if i % 2 != 0:
        for j in range(n - (i - 1) // 2, 0, -1):
            print('*', end=' ')
    else:
        for j in range(i // 2):
            print('*', end=' ')
    
    print()