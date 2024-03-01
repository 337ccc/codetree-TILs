n = int(input())

answer = 'P'
if n != 2:
    for i in range(2, n):
        if n % i == 0:
            answer = 'C'
            break

print(answer)