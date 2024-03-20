s, q = input().split()
s = list(s)
q = int(q)

for _ in range(q):
    type, a, b = input().split()
    type = int(type)

    if type == 1:
        a, b = int(a), int(b)
        s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
    else:
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
    
    answer = ''.join(s)
    print(answer)