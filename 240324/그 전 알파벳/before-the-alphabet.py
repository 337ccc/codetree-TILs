alphabet = input()

if alphabet == 'a':
    num = ord('z')
else:
    num = ord(alphabet)
    num -= 1

print(chr(num))