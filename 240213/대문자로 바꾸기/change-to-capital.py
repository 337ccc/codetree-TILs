arr = [input().split() for _ in range(5)]

for i in range(5):
    for j in range(3):
        arr[i][j] = arr[i][j].upper()  # upper : 대문자로 변경
    print(*arr[i])