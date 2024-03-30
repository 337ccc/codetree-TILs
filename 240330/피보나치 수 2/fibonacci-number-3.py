n = int(input())
fibo_lst = [0, 1]

if n != 1:
    for i in range(2, n + 1):
        answer = fibo_lst[i - 2] + fibo_lst[i - 1]
        fibo_lst.append(answer)

print(answer % 1000000007)