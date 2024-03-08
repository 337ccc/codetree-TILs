n = int(input())

for _ in range(n):
    answer = 1
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        answer *= i
    
    print(answer)