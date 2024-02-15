math_a, english_a = map(int, input().split())
math_b, english_b = map(int, input().split())

if math_a > math_b and english_a > english_b:
    print(1)
else:
    print(0)