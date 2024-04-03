def a_min_cost(possible_days):
    cost = 0
    coupon = 0
    
    # 먼저 5일권 구매
    new_possible_days = list(possible_days)
    for i in new_possible_days:
        if i in possible_days and i + 1 in possible_days and i + 2 in possible_days:
            if i + 3 in possible_days and i + 4 in possible_days:
                cost += 37000
                coupon += 2
                for j in range(i, i + 5):
                    possible_days.remove(j)
        else:
            continue

    # 그다음 3일권 구매
    new_possible_days = list(possible_days)
    for i in new_possible_days:
        if i in possible_days and i + 1 in possible_days and i + 2 in possible_days:
            cost += 25000
            coupon += 1
            for j in range(i, i + 3):
                possible_days.remove(j)
        else:
            continue

    # 마지막으로 1일권 구매
    possible_days_count = len(possible_days)
    for _ in range(possible_days_count):
        if coupon >= 3:
            coupon -= 3
        else:
            cost += 10000
    
    return cost

def b_min_cost(possible_days):
    cost = 0
    change_coupon = 0
    for i in range(1, 99):
        if i in possible_days:
            count = 0
            for j in range(i, i + 5):
                if j in possible_days:
                    count += 1
            if count >= 4:
                cost += 37000
                change_coupon += 2
                for j in range(i, i + 5):
                    if j in possible_days:
                        possible_days.remove(j)

            elif i in possible_days and i + 1 in possible_days and i + 2 in possible_days:
                cost += 25000
                change_coupon += 1
                for j in range(i, i + 3):
                    possible_days.remove(j)

            else:
                if change_coupon != 3:
                    cost += 10000
                possible_days.remove(i)

        else:
            if len(possible_days) == 0:
                return cost
            else:
                continue

n, m = map(int, input().split())
remove_days = list(map(int, input().split()))

possible_days = set(i for i in range(1, n + 1))
for i in remove_days:
    possible_days.remove(i)

a_possible_days = possible_days.copy()
b_possible_days = possible_days.copy()

answer_a = a_min_cost(a_possible_days)
answer_b = b_min_cost(b_possible_days)

if answer_a <= answer_b:
    print(answer_a)
else:
    print(answer_b)