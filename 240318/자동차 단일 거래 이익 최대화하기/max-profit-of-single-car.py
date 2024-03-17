n = int(input())
arr = list(map(int, input().split()))

max_profit = 0
for i in range(n - 1):
    buy = arr[i]
    sell = 0

    for j in range(i + 1, n):
        if buy < arr[j] and sell < arr[j]:
            sell = arr[j]
    
    if max_profit < sell - buy:
        max_profit = sell - buy

print(max_profit)