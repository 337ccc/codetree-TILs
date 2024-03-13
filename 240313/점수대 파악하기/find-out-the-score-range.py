score = list(map(int, input().split()))

ten = [0] * 11
for i in score:
    i //= 10
    ten[i] += 1

for j in range(10, 0, -1):
    print(f'{10 * j} - {ten[j]}')