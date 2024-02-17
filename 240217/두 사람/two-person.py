age_a, sex_a = input().split()
age_b, sex_b = input().split()

age_a = int(age_a)
age_b = int(age_b)

if (age_a >= 19 and sex_a == 'M') or (age_b >= 19 and sex_b == 'M'):
    print(1)
else:
    print(0)