word = input()
alphabet = input()

order = 1
for i in word:
    if i == alphabet:
        print(order)
        break
    else:
        order += 1

if order == len(word):
    print('Not Found')