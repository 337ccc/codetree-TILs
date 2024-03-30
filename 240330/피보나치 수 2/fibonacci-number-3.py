n = int(input())
fibo_dict = {0:0, 1:1}

if n != 1:
    for i in range(2, n + 1):
        fibo_dict[i] = fibo_dict[i - 2] + fibo_dict[i - 1]

print(fibo_dict[n] % 1000000007)