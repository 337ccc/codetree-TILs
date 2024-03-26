A = input()
B = input()

num_A, num_B = '', ''
for i in A:
    if i.isdigit() == True:
        num_A += i

for j in B:
    if j.isdigit() == True:
        num_B += j

num_A, num_B = int(num_A), int(num_B)
print(num_A + num_B)