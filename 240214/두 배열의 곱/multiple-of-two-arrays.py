matrix1 = [list(map(int, input().split())) for _ in range(3)]
blank = input()
matrix2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        num = matrix1[i][j] * matrix2[i][j]
        print(num, end=' ')
    print()