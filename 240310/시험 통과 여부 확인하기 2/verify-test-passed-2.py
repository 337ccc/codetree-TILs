n = int(input())

count = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    average_grade = sum(arr) / 4
    if average_grade >= 60:
        print('pass')
        count += 1
    else:
        print('fail')

print(count)