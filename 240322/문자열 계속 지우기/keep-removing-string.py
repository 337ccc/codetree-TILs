A = input()
B = input()

while B in A:
    order = A.index(B)
    front = A[:order]
    back = A[order + len(B):]
    A = front + back

print(A)