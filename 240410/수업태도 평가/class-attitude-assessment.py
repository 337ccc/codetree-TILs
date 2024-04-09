student = {
    'Bessie' : 0,
    'Elsie' : 0,
    'Daisy' : 0,
    'Gertie' : 0,
    'Annabelle' : 0,
    'Maggie' : 0,
    'Henrietta' : 0
    }

n = int(input())
for _ in range(n):
    name, score = input().split()
    score = int(score)
    student[name] = score

final_score_lst = [
    student['Bessie'],
    student['Elsie'],
    student['Daisy'],
    student['Gertie'],
    student['Annabelle'],
    student['Maggie'],
    student['Henrietta']
    ]

student_score_lst = [
    ['Bessie', student['Bessie']],
    ['Elsie', student['Elsie']],
    ['Daisy', student['Daisy']],
    ['Gertie', student['Gertie']],
    ['Annabelle', student['Annabelle']],
    ['Maggie', student['Maggie']],
    ['Henrietta', student['Henrietta']]
    ]

smallest = min(final_score_lst)
# 모든 학생의 점수가 같다면 Tie 출력
if final_score_lst.count(smallest) == 7:
    print('Tie')

else:
    while smallest in final_score_lst:
        final_score_lst.remove(smallest)
    smallest = min(final_score_lst)
    # 두 번째로 낮은 학생이 여러 명이면
    if final_score_lst.count(smallest) >= 2:
        print('Tie')
    else:
        for i in student_score_lst:
            if i[1] == smallest:
                print(i[0])