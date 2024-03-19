n, m = map(int, input().split())
matrix = [list(0 for _ in range(n)) for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = r * c

for line in matrix:
    print(*line)