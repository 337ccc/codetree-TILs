n = int(input())

num = 64
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    
    for j in range(n - i, 0, -1):
        if num == 90:
            num = 65
        else:
            num += 1
        print(chr(num), end=' ')
    
    print()