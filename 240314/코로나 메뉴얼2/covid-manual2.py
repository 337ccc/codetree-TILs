patience = [0 for i in range(4)]
emer = 0

for _ in range(3):
    sym, temp = input().split()
    temp = int(temp)
    
    if sym == 'Y':
        if temp >= 37:
            patience[0] += 1
            emer += 1
        else:
            patience[2] += 1
    else:
        if temp >= 37:
            patience[1] += 1
        else:
            patience[3] += 1
    
print(*patience, end=' ')

if emer >= 2:
    print('E')