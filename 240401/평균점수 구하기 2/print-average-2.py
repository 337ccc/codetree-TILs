n = int(input())
score_lst = list(map(float, input().split()))

print(f'{sum(score_lst) / len(score_lst):.1f}')