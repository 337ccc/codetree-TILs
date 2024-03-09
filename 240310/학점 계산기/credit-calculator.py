n = int(input())
grade = list(map(float, input().split()))

average_grade = sum(grade) / n
if average_grade >= 4.0:
    answer = 'Perfect'
elif average_grade >= 3.0:
    answer = 'Good'
else:
    answer = 'Poor'

print(f'{average_grade:.1f}')
print(answer)