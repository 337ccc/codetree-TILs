n, m = map(int, input().split())
matrix = [list(0 for _ in range(n)) for _ in range(n)]

for i in range(1, m + 1):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = i

for line in matrix:
    print(*line)