arr = list(map(int, input().split()))

answer = []
for i in arr:
    if i != 0:
        if i % 2 != 0:
            i += 3
        else:
            i //= 2    
        answer.append(i)
    
    else:
        break

print(*answer)