word = input()

for i in range(len(word)):
    if word[i] == 'e':
        answer = word[:i] + word[i + 1:]
        print(answer)
        break