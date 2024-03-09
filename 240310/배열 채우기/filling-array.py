arr = list(map(int, input().split()))

answer = []
for i in arr:
    if i != 0:
        answer.append(i)
    else:
        break

print(*answer[::-1])