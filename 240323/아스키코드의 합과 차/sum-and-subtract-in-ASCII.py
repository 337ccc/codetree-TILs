# ord('A') -> 65

a, b = input().split()
a_num = ord(a)
b_num = ord(b)

print(a_num + b_num, abs(a_num - b_num))