alphabet = input()

if alphabet == 'z':
    num = ord('a')
else:
    num = ord(alphabet)
    num += 1

print(chr(num))