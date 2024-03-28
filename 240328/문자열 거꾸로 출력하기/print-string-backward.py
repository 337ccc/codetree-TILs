status = True
while status == True:
    word = input()
    if word == 'END':
        status = False
    else:
        word = word[::-1]
        print(word)