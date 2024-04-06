n = int(input())
element_lst = list(map(int, input().split()))

num = min(element_lst)
for i in range(1, num + 1):
    if num % i == 0:
        print(i)