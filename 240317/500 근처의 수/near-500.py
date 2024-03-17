arr = list(map(int, input().split()))

max_num = 0
min_num = 1001
for i in arr:
    if max_num < i and i < 500:
        max_num = i
    elif min_num > i and i > 500:
        min_num = i

print(max_num, min_num)