A = input()
order_lst = list(input())

for order in order_lst:
    if order == 'L':
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]

print(A)