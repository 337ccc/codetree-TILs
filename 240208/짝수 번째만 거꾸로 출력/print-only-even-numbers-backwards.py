word = list(input())

new_word = ''
for i in range(len(word) // 2, 0, -1):
    new_word += word[2 * i  - 1]
print(new_word)