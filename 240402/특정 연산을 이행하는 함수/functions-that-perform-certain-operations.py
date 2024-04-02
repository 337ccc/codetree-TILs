num_lst = list(map(int, input().split()))

for i in num_lst:
    if i % 2 == 0:
        print(i // 2, end=' ')
    else:
        print(i * 3 - 20, end=' ')