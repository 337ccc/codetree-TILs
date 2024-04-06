a, b, c = map(int, input().split())
num_lst = [a, b, c]
count = 0
total = 1
for i in num_lst:
    if i % 2 != 0:
        count += 1
        total *= i

if count != 0:
    print(total)
else:
    print(a * b * c)