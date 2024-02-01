alphabet = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]
new_arr = []

for word in arr:
    if word[2] == alphabet or word[3] == alphabet:
        new_arr.append(word)

new_arr.append(len(new_arr))

for i in new_arr:
    print(i)