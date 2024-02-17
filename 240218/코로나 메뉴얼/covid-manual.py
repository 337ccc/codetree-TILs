Symptom_first, temp_first = input().split()
Symptom_second, temp_second = input().split()
Symptom_third, temp_third = input().split()

emergency = 0
arr_symptom = [Symptom_first, Symptom_second, Symptom_third]
arr_temp = [temp_first, temp_second, temp_third]

for i in range(3):
    if arr_symptom[i] == 'Y' and int(arr_temp[i]) >= 37:
        emergency += 1

if emergency >= 2:
    print('E')
else:
    print('N')