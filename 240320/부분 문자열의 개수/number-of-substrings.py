A = input()
B = input()

count_B = 0
for i in range(len(A) - 1):
    if A[i] == B[0] and A[i + 1] == B[1]:
        count_B += 1

print(count_B)