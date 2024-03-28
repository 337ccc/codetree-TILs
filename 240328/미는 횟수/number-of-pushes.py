A = input()
B = input()

count = 0
if len(A) != len(B):
    count = -1
else:
    while A != B:
        A = A[-1] + A[:-1]
        count += 1
        if count == len(A):
            count = -1
            break

print(count)