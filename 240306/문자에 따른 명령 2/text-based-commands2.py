order = list(input())

now_y = 0
now_x = 0

# 북, 서, 남, 동
dir_y = [1, 0, -1, 0]
dir_x = [0, -1, 0, 1]

dir_order = 0
for i in order:
    if i == 'L':
        if dir_order == 3:
            dir_order = 0
        else:
            dir_order += 1
    elif i == 'R':
        if dir_order == 0:
            dir_order = 3
        else:
            dir_order -= 1
    else:
        now_y += dir_y[dir_order]
        now_x += dir_x[dir_order]

print(now_x, now_y)