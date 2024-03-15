a, b = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

answer = 'No'
for i in range(len(list_A)):
    new_list = []
    # A 안에 B의 첫번째 원소가 들어가 있다면, 부분집합일 가능성 있음
    # 부분집합인지 아닌지 확인하는 과정에서 A를 넘어가지 않아야 함
    if list_A[i] == list_B[0] and len(list_A) >= i + len(list_B):
        # B 안의 원소들 하나씩 확인하며 부분집합인지 확인
        for j in range(len(list_B)):
            if list_B[j] == list_A[i + j]:
                new_list.append(list_A[i + j])
            
            if list_B == new_list:
                answer = 'Yes'
                break

print(answer)