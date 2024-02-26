count = 0

while count != 3:
    num = int(input())
    if num % 2 == 0:
        num //= 2
        count += 1
        print(num)