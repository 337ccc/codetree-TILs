n, m = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = 1

for line in matrix:
    print(*line)