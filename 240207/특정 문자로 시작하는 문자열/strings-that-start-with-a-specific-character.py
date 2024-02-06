arr = []
count = 0  # 문자열의 개수
total = 0  # 문자열 길이의 총합

n = int(input())
for _ in range(n):
    arr.append(input())
alphabet = input()

for i in range(n):
    word = list(arr[i])
    if word[0] == alphabet:
        count += 1
        total += len(arr[i])

print(f'{count} {total / count:.2f}')