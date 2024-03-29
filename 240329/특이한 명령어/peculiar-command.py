n = int(input())

for _ in range(n):
    int_a, int_b, alpha = input().split()
    int_a, int_b = int(int_a), int(int_b)

    if alpha == 's':
        answer = int_a * int_b
        print(answer)
    elif alpha == 't':
        answer = int_a * int_b / 2
        print(f'{answer:.1f}')