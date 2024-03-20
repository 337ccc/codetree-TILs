first, second = input().split()
second = list(second)

second[0] = first[0]
second[1] = first[1]
answer = ''.join(second)
print(answer)