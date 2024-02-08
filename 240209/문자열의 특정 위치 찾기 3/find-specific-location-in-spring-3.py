word = input()
alphabet = input()

order = 1
for i in word:
    if i != alphabet:
        order += 1
    else:
        print(order)
        break

if order == len(word):
    print('Not Found')