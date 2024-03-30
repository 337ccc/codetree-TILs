n = int(input())
fibo_lst = [0, 1]

if n != 1:
    for i in range(2, n + 1):
        fibo_lst.append(fibo_lst[i - 2] + fibo_lst[i - 1])

print(fibo_lst[n])