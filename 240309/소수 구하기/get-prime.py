n = int(input())

if n != 1:
    for i in range(2, n + 1):
        result = 0
        for j in range(2, i + 1):
            if i % j == 0:
                result += 1
        
        if result == 1:
            print(i, end=' ')