arr = [list(map(int, input().split())) for _ in range(4)]

total = 0
for i in range(4):
    line_sum = sum(arr[i][0:i + 1])
    total += line_sum

print(total)