a, b = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

answer = 'No'
for i in range(len(list_A)):
    new_list = []
    if list_A[i] == list_B[0]:
        for j in range(len(list_B)):
            if list_B[j] == list_A[i + j]:
                new_list.append(list_A[i + j])
            
            if list_B == new_list:
                answer = 'Yes'
                break

print(answer)