N = int(input())
arr = list(map(int, input().split()))

max_num = 0
index_arr = []
for i in range(N):
    if arr[i] > max_num:
        max_num = arr[i]
        index_arr.append(i + 1)

index_arr.sort(reverse=True)
print(*index_arr)