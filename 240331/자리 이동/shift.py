def count_arrangements(n, m, fixed_positions):
    # 고정칸에 배치해야 할 수
    fixed_values = set(range(1, n + 1))

    # 고정칸에 있는 수를 확인하고 제거
    for pos in fixed_positions:
        fixed_values.remove(pos)

    # 가능한 수들의 리스트
    available_values = list(fixed_values)

    # 가능한 수들의 순열을 구하는 재귀 함수
    def permute(arr, perm, result):
        if len(perm) == len(arr):
            result.append(perm.copy())
        else:
            for i in range(len(arr)):
                if not perm or abs(arr[i] - perm[-1]) <= 1:
                    perm.append(arr[i])
                    permute(arr, perm, result)
                    perm.pop()

    permutations = []
    permute(available_values, [], permutations)

    # 고정칸에 배치된 수와 가능한 수들의 순열을 조합하여 경우의 수 계산
    total_count = 0
    for perm in permutations:
        arrangement = list(fixed_positions)
        index = 0
        for i in range(n):
            if i + 1 not in fixed_positions:
                arrangement.append(perm[index])
                index += 1
        valid = True
        for i in range(1, n):
            if abs(arrangement[i] - arrangement[i - 1]) > 1:
                valid = False
                break
        if valid:
            total_count += 1

    return total_count


# 입력 받기
n, m = map(int, input().split())
fixed_positions = list(map(int, input().split()))

# 경우의 수 계산 및 출력
result = count_arrangements(n, m, fixed_positions)
print(result)