lst = list(map(int, input().split()))

total_two = 0
for i in lst[1::2]:
    total_two += i

total_three = 0
count = 0
for j in lst[2::3]:
    total_three += j
    count += 1

print(total_two, f'{total_three / count:.1f}')