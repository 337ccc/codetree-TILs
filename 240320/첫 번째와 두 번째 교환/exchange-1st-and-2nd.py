word = list(input())
first = word[0]
second = word[1]

for i in range(len(word)):
    if word[i] == first:
        word[i] = second
    elif word[i] == second:
        word[i] = first

answer = ''.join(word)
print(answer)