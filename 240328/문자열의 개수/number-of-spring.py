status = True
order = 0
odd_lst = []
while status == True:
    word = input()
    if word == '0':
        status = False
    else:
        order += 1
        if order % 2 != 0:
            odd_lst.append(word)

print(order)
for i in odd_lst:
    print(i)