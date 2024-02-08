n = int(input())
number_arr = input().split()

number = ''
for i in number_arr:
    number += i

line = len(number) // 5
for i in range(line):
    print(number[i * 5 : i * 5 + 5])

if len(number) % 5 != 0:
    print(number[line * 5 : len(number)])