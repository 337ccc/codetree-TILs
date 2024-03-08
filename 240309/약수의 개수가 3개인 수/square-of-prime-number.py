start, end = map(int, input().split())

count = 0
for i in range(start, end + 1):
    divisor_count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divisor_count += 1
            # 약수의 개수가 3 초과라면 시간 절약을 위해 코드 추가
            if divisor_count > 3:
                continue
    
    if divisor_count == 3:
        count += 1
    
print(count)