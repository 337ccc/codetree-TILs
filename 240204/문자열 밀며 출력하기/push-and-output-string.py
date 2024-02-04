word = input()

arr = list(word)

for i in range(len(arr) + 1):
    new_word = ''
    for j in range(len(arr)):
        new_word += arr[j - len(arr) + i]
    print(new_word)