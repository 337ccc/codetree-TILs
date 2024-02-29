n = int(input())

result = 'N'
if n == 2:
    print(result)
else:
    for i in range(2, n):
        if n % i == 0:
            result = 'C'
            break

print(result)