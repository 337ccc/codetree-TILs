n = int(input())

answer = 0
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end=' ')
    for j in range(i):
        if answer == 9:
            answer = 1
        else:
            answer += 1
        print(answer, end=' ')
    
    print()