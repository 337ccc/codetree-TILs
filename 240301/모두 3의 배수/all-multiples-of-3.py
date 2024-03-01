answer = 1
for _ in range(5):
    num = int(input())
    if num % 3 != 0:
        answer = 0
        break

print(answer)