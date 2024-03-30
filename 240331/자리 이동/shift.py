n, m = map(int, input().split())
fixed_lst = list(map(int, input().split()))

seat_lst = [0 for _ in range(n)]
for i in fixed_lst:
    seat_lst[i - 1] = i

print(seat_lst)