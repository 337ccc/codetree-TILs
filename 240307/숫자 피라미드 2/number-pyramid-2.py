n = int(input())

answer = 0
for i in range(1, n + 1):
    for j in range(i):
        answer += 1
        print(answer, end=' ')
    
    print()