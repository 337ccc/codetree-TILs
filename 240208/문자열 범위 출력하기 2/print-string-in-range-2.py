word = list(input())
n = int(input())

new_word = ''
if n > len(word):
    # 주어진 정수가 문자열의 길이보다 크다면 문자열을 모두 출력
    for i in range(len(word) - 1, -1, -1):
        new_word += word[i]
else:
    for i in range(len(word) - 1, len(word) - 1 - n, -1):
        new_word += word[i]

print(new_word)