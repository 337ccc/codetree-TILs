word = input()
alphabet = input()

order = 0
for i in word:
    if i == alphabet:
        print(order + 1)
        break
    else:
        order += 1

if order == len(word):
    print('Not Found')