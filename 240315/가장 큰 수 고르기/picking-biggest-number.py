arr = list(map(int, input().split()))

max_num = 0
for i in arr:
    if i > max_num:
        max_num = i

print(max_num)