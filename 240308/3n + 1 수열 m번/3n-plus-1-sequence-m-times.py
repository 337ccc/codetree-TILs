m = int(input())

for _ in range(m):
    n = int(input())
    total = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
            total += 1
        else:
            n = (3 * n) + 1
            total += 1
    
    print(total)