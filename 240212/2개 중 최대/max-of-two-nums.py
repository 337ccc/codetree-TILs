# 삼항연산자를 이용한 코드
# a = v1(참일 경우의 값) if 조건 else v2(거짓일 경우의 값)

a, b = map(int, input().split())

answer = a if a >= b else b
print(answer)