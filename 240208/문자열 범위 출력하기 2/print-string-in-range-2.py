word = list(input())
n = int(input())

new_word = ''
for i in range(len(word)-1, len(word)-1-n, -1):
    new_word += word[i]

print(new_word)