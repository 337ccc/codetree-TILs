total = 0
count = 0

while True:
    age = int(input())
    if age == 100 or age // 10 != 2:
        break
    total += age
    count += 1

print(f'{total / count:.2f}')