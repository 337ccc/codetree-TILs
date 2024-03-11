arr = list(map(int, input().split()))

sum_odd = 0
sum_even = 0
for i in range(10):
    if i % 2 == 0:
        sum_odd += arr[i]
    else:
        sum_even += arr[i]

print(abs(sum_odd - sum_even))