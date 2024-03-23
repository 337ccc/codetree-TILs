word, num = input().split()
num = int(num)

for i in range(num):
    type = int(input())
    if type == 1:
        word = word[1:] + word[0]
    elif type == 2:
        word = word[-1] + word[:-1]
    else:
        word = word[::-1]
    print(word)