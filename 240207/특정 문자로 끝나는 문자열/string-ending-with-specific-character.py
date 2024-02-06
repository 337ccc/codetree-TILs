arr = []
count = 0

for _ in range(10):
    arr.append(input())

alphabet = input()

for i in arr:
    alpha_arr = list(i)
    if alpha_arr[-1] == alphabet:
        print(i)
        count += 1

if count == 0:
    print('None')