n = int(input())

for i in range(n):
    num = i + 1
    for j in range(n):
        answer = num + n * j
        print(answer, end=' ')
    print()