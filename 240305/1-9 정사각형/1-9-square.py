n = int(input())

answer = 0
for i in range(n):
    for j in range(n):
        if answer == 9:
            answer = 1
        else:
            answer += 1
        print(answer, end='')
    
    print()