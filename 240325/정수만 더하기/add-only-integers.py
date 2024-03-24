word = input()

answer = 0
for i in word:
    if i.isdigit() == True:
        answer += int(i)

print(answer)