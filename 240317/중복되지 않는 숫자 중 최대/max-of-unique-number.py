N = int(input())
arr = list(map(int, input().split()))

# set을 통해 중복되는 것 제거하고 어떤 element가 있는지 확인
repeat_check = set(arr)
repeat_check = list(repeat_check)
max_num = 0
for i in repeat_check:
    # 몇 개인지
    number = arr.count(i)
    if number == 1:
        if max_num < i:
            max_num = i

if max_num == 0:
    max_num = -1

print(max_num)