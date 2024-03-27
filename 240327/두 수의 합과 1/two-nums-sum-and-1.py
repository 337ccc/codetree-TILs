a, b = map(int, input().split())

num = a + b
num = str(num)
count = 0
for i in num:
    if i == '1':
        count += 1

print(count)