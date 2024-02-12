arr = [list(map(int, input().split())) for _ in range(2)]

line_average1 = sum(arr[0]) / 4
line_average2 = sum(arr[1]) / 4

row_average1 = (arr[0][0] + arr[1][0]) / 2
row_average2 = (arr[0][1] + arr[1][1]) / 2
row_average3 = (arr[0][2] + arr[1][2]) / 2
row_average4 = (arr[0][3] + arr[1][3]) / 2

total_average = (sum(arr[0]) + sum(arr[1])) / 8

print(f'{line_average1:.1f} {line_average2:.1f}')
print(f'{row_average1:.1f} {row_average2:.1f} {row_average3:.1f} {row_average4:.1f}')
print(f'{total_average:.1f}')