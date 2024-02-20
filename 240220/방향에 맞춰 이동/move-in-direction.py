N = int(input())

# 서, 남, 북, 동
dir_y = [0, -1, 1, 0]
dir_x = [-1, 0, 0, 1]

location_y, location_x = 0, 0
for i in range(N):
    dir, length = input().split()
    if dir == 'W':
        num = 0
    elif dir == 'S':
        num = 1
    elif dir == 'N':
        num = 2
    else:
        num = 3
    length = int(length)
    location_y += dir_y[num] * length
    location_x += dir_x[num] * length

print(location_x, location_y)