A, B = map(int, input().split())

gap = abs(A - B)
now_dir = 'R'
now = 1
total = 1

if A - B < 0:
    dir = 'L'
else:
    dir = 'R'

if gap != 1:
    while now_dir == dir or gap > now:
        if gap < now * 2:
            total += (now + gap)
        else:
            total += (now + now * 2)
        now *= 2

        if now_dir == 'R':
            now_dir = 'L'
        else:
            now_dir = 'R'

print(total)