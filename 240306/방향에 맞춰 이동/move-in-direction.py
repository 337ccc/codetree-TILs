N = int(input())

# 서, 남, 북, 동
dir_y = [0, -1, 1, 0]
dir_x = [-1, 0, 0, 1]

now_y, now_x = 0, 0
for _ in range(N):
    dir, num = input().split()
    num = int(num)
    if dir == 'W':
        now_y += dir_y[0] * num
        now_x += dir_x[0] * num
    elif dir == 'S':
        now_y += dir_y[1] * num
        now_x += dir_x[1] * num
    elif dir == 'N':
        now_y += dir_y[2] * num
        now_x += dir_x[2] * num
    else:
        now_y += dir_y[3] * num
        now_x += dir_x[3] * num

print(now_x, now_y)