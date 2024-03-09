# arr[start:end:step]
# arr[::-1] # 전체 원소 뒤집기

arr = input().split()

answer = ''
for i in arr[::-1]:
    answer += i

print(answer)