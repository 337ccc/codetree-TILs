arr = list(map(int, input().split()))

number = [0] * 6
for i in arr:
    number[i - 1] += 1

for j in range(6):
    print(f'{j + 1} - {number[j]}')