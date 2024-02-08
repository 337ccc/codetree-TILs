word = list(input())
n = int(input())

new_word = ''
if n > len(word):
    for i in range(len(word) - 1, -1, -1):
        new_word += word[i]
else:
    for i in range(len(word) - 1, len(word) - 1 - n, -1):
        new_word += word[i]

print(new_word)