word, alhapbet = input().split()

answer = word.find(alhapbet)

if answer == -1:
    print('No')
else:
    print(answer)