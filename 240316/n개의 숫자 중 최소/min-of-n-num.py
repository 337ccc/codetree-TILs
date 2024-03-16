N = int(input())
arr = list(map(int, input().split()))

min_num = 2 ** 31
for i in arr:
    if i <= min_num:
        min_num = i

print(min_num, arr.count(min_num))