height, weight = map(int, input().split())

height_m = height / 100
bmi = weight // height_m ** 2

print(f'{bmi:.0f}')

if bmi >= 25:
    print('Obesity')