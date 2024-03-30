n = int(input())

now = 1000
count = 0
num = 0
total = 0
while now > n:
    count += 1
    num += 2
    now -= num
    total += num

print(count, total)