left, right = input().split()

a = len(left)
b = len(right)

if a > b:
    print(left, a)
elif a < b:
    print(right, b)
else:
    print('same')