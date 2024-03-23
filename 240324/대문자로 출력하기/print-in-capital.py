lst = list(input())

answer = ''
for i in lst:
    if i.isalpha() == True:
        answer += i.upper()

print(answer)