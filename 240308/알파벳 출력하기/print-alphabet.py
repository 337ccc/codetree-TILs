n = int(input())

num = 64
for i in range(1, n + 1):
    for j in range(i):
        num += 1
        print(chr(num), end='')
    
    print()