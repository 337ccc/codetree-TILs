n = int(input())

answer = 0
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            answer += 1
        else:
            answer = n * (i + 1) - j
        print(answer, end=' ')

    print()