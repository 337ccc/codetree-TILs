n, q = map(int, input().split())
factor = list(map(int, input().split()))

for _ in range(q):
    quest = list(map(int, input().split()))
    if quest[0] == 1:
        print(factor[quest[1] - 1])
    elif quest[0] == 2:
        if quest[1] in factor:
            print(factor.index(quest[1]) + 1)
    else:
        a = quest[1]
        b = quest[2]
        print(*factor[a - 1:b])