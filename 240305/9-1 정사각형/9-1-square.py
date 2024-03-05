n = int(input())

answer = 10
for i in range(n):
    for j in range(n):
        if answer == 1:
            answer = 9
        else:
            answer -= 1
        print(answer, end='')
    
    print()