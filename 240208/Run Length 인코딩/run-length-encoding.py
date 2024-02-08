word = list(input())

before_alpha = word[0]
new_word = ''
count = 1
for i in range(1, len(word)):
    if before_alpha == word[i]:
        count += 1
        if i == len(word) - 1:
            new_word += before_alpha
            new_word += str(count)
    else:
        new_word += before_alpha
        new_word += str(count)
        # 새로운 알파벳으로 초기화, count도 1로 바꾸기
        before_alpha = word[i]
        count = 1
        if i == len(word) - 1:
            new_word += before_alpha
            new_word += '1'

print(len(new_word))
print(new_word)