arr = list(map(int, input().split()))

answer = 0
for i in range(10):
    if arr[i] >= 250:
        print(sum(arr[:i]), f'{sum(arr[:i])/i:.1f}')
        answer += 1
        break
    
if answer == 0:
    print(sum(arr), f'{sum(arr)/10:.1f}')