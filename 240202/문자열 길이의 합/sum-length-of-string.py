N = int(input())

new_word = ''
count = 0

for i in range(N):
    word = input()
    new_word += word
    if word[0] == 'a':
        count += 1

print(len(new_word), count)