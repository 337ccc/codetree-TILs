three = 0
five = 0
for _ in range(10):
    num = int(input())
    if num % 15 == 0:
        three += 1
        five += 1
    elif num % 3 == 0:
        three += 1
    elif num % 5 == 0:
        five += 1

print(three, five)