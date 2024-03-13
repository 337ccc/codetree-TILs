n = int(input())
arr = list(map(int, input().split()))

number = [0] * 10
for i in arr:
    number[i] = number[i] + 1

for j in range(1, 10):
    print(number[j])