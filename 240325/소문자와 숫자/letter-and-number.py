word = input()

answer = ''
for i in word:
    if i.isdigit() == True:
        answer += i
    elif i.isalpha() == True:
        answer += i.lower()

print(answer)