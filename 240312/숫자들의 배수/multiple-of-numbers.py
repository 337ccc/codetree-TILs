n = int(input())

_list = []
count = 0
for i in range(1, 11):
    num = i * n
    _list.append(num)
    
    if num % 5 == 0:
        count += 1
    
    if count == 2:
        break

print(*_list)