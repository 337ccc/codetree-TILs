A, B = map(int, input().split())

# A와 B의 거리
gap = abs(A - B)
now_dir = 'R'
now = 1
total = 1

# A가 B를 향하는 방향
if A - B < 0:
    dir = 'L'
else:
    dir = 'R'

if gap != 1:
    while now_dir == dir or gap > now:
        if gap < now * 2 and dir == now_dir:
            total += (now + gap)
        else:
            total += (now + now * 2)
        now *= 2

        if now_dir == 'R':
            now_dir = 'L'
        else:
            now_dir = 'R'

print(total)