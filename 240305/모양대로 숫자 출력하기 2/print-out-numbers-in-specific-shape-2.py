n = int(input())

answer = 0
for i in range(n):
    for j in range(n):
        if answer == 8:
            answer = 2
        else:
            answer += 2
        print(answer, end=' ')
    
    print()