arr = list(map(int, input().split()))

ten = [0] * 10
for i in arr:
    if i == 0:
        break
    else:
        i //= 10
        ten[i] += 1

for j in range(1, 10):
    print(f'{j} - {ten[j]}')