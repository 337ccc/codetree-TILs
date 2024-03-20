word = list(input())

word.pop(1)
word.pop(-2)
answer = ''.join(word)
print(answer)