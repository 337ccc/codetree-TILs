num_lst = list(i for i in range(1, 31))

for _ in range(28):
    num = int(input())
    num_lst.remove(num)

print(min(num_lst))
print(max(num_lst))