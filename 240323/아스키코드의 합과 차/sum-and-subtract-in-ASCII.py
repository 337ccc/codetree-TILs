# ord('A') -> 65

a, b = input().split()
a_num = ord(a)
b_num = ord(b)
if a_num > b_num:
    minus = a_num - b_num
else:
    minus = b_num - a_num

print(a_num + b_num, minus)