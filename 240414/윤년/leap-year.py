year = int(input())

if year % 400 == 0:
    answer = 1
elif year % 100 == 0:
    answer = 0
elif year % 4 == 0:
    answer = 1
else:
    answer = 0

print(answer)