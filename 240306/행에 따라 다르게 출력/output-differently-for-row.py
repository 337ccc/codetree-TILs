n = int(input())

answer = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % 2 != 0:
            answer += 1
        else:
            answer += 2
        print(answer, end=' ')
    
    print()