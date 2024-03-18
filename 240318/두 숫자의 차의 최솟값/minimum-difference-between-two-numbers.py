n = int(input())
arr = list(map(int, input().split()))

min_difference = 99
for i in range(n - 1):
    for j in range(i + 1, n):
        difference = abs(arr[i] - arr[j])
        
        if min_difference > difference:
            min_difference = difference

print(min_difference)