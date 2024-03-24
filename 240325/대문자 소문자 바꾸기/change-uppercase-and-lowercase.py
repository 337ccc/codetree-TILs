word = input()

answer = ''
for i in word:
    if i != i.upper():
        answer += i.upper()
    else:
        answer += i.lower()

print(answer)