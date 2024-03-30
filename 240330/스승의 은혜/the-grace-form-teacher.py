def max_students(N, B, students):
    students.sort(key=lambda x: (x[0], x[1]))  # 선물의 가격을 기준으로 학생들을 정렬

    total_cost = 0
    count = 0

    for i in range(N):
        price, shipping = students[i]
        total_cost += (price + shipping)  # 현재 학생이 선택된 경우의 총 비용에 가격을 추가

        # 선생님이 쿠폰을 사용하는 경우
        if i % 2 == 1:
            total_cost -= price / 2  # 가장 저렴한 선물에 대한 반값 할인

        # 총 비용이 예산을 초과하는 경우, 이전 학생들을 선택해야 함
        if total_cost > B:
            break

        count += 1

    return count

# 입력 받기
N, B = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_students(N, B, students))