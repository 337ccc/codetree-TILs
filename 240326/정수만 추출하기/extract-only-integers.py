A, B = input().split()

num_A = ''
num_B = ''

for i in A:
    if i.isdigit() == True:
        num_A += i
    else:
        break

for j in B:
    if j.isdigit() == True:
        num_B += j
    else:
        break

num_A, num_B = int(num_A), int(num_B)
print(num_A + num_B)