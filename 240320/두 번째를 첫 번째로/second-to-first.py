arr = list(input())
first = arr[0]
second = arr[1]

for i in range(len(arr)):
    if arr[i] == second:
        arr[i] = first

answer = ''.join(arr)
print(answer)