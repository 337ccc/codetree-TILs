first, first_remain = map(int, input().split())
second, second_remain = map(int, input().split())
third, third_remain = map(int, input().split())

now = 'first'
for _ in range(100):
    if now == 'first':
        now = 'second'
        if second - second_remain >= first_remain:
            second_remain += first_remain
            first_remain = 0
        else:
            first_remain -= (second - second_remain)
            second_remain = second
    elif now == 'second':
        now = 'third'
        if third - third_remain >= second_remain:
            third_remain += second_remain
            second_remain = 0
        else:
            second_remain -= (third - third_remain)
            third_remain = third
    elif now == 'third':
        now = 'first'
        if first - first_remain >= third_remain:
            first_remain += third_remain
            third_remain = 0
        else:
            third_remain -= (first - first_remain)
            first_remain = first

print(first_remain)
print(second_remain)
print(third_remain)