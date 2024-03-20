word = input()

count_ee = 0
count_eb = 0
for i in range(len(word) - 1):
    if word[i] == 'e':
        if word[i + 1] == 'e':
            count_ee += 1
        elif word[i + 1] == 'b':
            count_eb += 1

print(count_ee, count_eb)