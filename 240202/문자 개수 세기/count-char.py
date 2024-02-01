arr = input()
alphabet = input()

count = 0
for i in arr:
    if i == alphabet:
        count += 1

print(count)