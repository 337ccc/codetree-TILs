# 2n개의 줄이 있다고 생각하고
# 홀수번째와 짝수번째로 나눠서 생각하기

n = int(input())

for i in range(1, 2 * n + 1):
    if i % 2 != 0:
        for j in range((i + 1) // 2):
            print('*', end=' ')
    else:
        for j in range((n + 1) - i // 2, 0, -1):
            print('*', end=' ')
    
    print()