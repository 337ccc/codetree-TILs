a, b = map(int, input().split())

answer_sum = 0
count = 0
for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        answer_sum += i
        count += 1

print(f'{answer_sum} {answer_sum / count:.1f}')