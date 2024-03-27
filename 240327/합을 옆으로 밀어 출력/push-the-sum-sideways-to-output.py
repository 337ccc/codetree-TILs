n = int(input())

total = 0
for _ in range(n):
    element = int(input())
    total += element

total = str(total)
total = total[1:] + total[0]
print(total)