word = input()
alphabet = input()

count = 0
for i in word:
    if i == alphabet:
        print(count)
        break
    else:
        count += 1

if count == len(word):
    print('Not Found')