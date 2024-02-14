n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            num = 0
        else:
            num = 1
        print(num, end=' ')
    print()