n = int(input())

count = 0
for i in range(1, n + 1):
    # 해당 조건에 해당하면 다시 처음으로 돌아감
    # count += 1 코드 실행하지 않음
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    count += 1

print(count)