def max_students(N, B, students):
    # 선물 가격과 배송비의 합을 기준으로 올림차순으로 학생들을 정렬
    students.sort(key=lambda x: x[0] + x[1])
    # 선물 가격을 기준으로 올림차순으로 학생들을 정렬
    # students.sort(key=lambda x: (x[0], x[1]))

    total_cost = 0
    count = 0

    for i in range(N):
        # 선물 가격, 배송비
        price, shipping = students[i]
        total_cost += (price + shipping)

        # 예산보다 총비용이 더 많이 나왔다면
        if total_cost > B:
            # 반값 할인 적용해보기
            total_cost -= price / 2
            # 반값 할인 적용했는데도 예산보다 높다면 그 학생부턴 선물 주지 못함
            if total_cost > B:
                break
            else:
                count += 1
                break

        count += 1

    return count

N, B = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]

print(max_students(N, B, students))