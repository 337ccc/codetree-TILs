n = int(input())
score_lst = list(map(int, input().split()))

range_lst = {10:0, 20:0, 30:0, 40:0, 40:0, 50:0, 60:0, 70:0, 80:0, 90:0, 100:0}
for i in score_lst:
    if i < 10:
        continue
    else:
        num_key = (i // 10) * 10
        num_value = range_lst[num_key] + 1
        range_lst[num_key] = num_value

for j in range(10, 0, -1):
    score = j * 10
    if range_lst[score] != 0:
        print(score, '-', range_lst[score])