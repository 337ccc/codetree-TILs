n = int(input())

alpha_count = 64
num_count = -1
for i in range(n + 1):
    for j in range(n - i, 0, -1):
        if alpha_count == 90:
            alpha_count = 65
        else:
            alpha_count += 1
        print(chr(alpha_count), end=' ')
    
    for j in range(0, i):
        if num_count == 9:
            num_count = 0
        else:
            num_count += 1
        print(num_count, end=' ')

    print()