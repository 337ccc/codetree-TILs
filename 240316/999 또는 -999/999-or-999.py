arr = list(map(int, input().split()))

max_num = -1000
min_num = 1000
for i in arr:
    if i == 999 or i == -999:
        break
    else:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i

print(max_num, min_num)