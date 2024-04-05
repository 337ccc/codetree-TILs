N = int(input())
time_lst = list(0 for _ in range(1001))
for _ in range(N):
    s, t, b = map(int, input().split())
    for i in range(s, t + 1):
        time_lst[i] += b

print(max(time_lst))