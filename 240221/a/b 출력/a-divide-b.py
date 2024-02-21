a, b = map(int, input().split())

count = 0
print(f'{a // b}.', end='')
while count <= 19:
    count += 1
    a = (a % b) * 10
    quota = a // b
    print(f'{quota}', end='')