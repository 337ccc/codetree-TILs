n = int(input())

arr = [[1], [1, 1]]

if n >= 3:
    n = n - 1  # 첫 번째 줄이 결국 0번째 인덱스이기 때문에 1을 빼고 시작
    for i in range(1, n):
        line = [1]
        for j in range(1, i + 1):
            num = arr[i][j - 1] + arr[i][j]
            line.append(num)
        line.append(1)
        arr.append(line)
    n = n + 1  # 1 뺐던 걸 다시 더해줌

for m in range(n):
    print(*arr[m])