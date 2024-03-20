word = list(input())

for _ in range(len(word) - 1):
    num = int(input())
    if num >= len(word):
        word.pop(-1)
    else:
        word.pop(num)
    answer = ''.join(word)
    print(answer)