n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j % 2 != 0 and i == 1:
            print('*', end = ' ')
        elif j % 2 == 0 and i <= j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    
    print()