N, M, K = map(int, input().split())

lattice = [list(input()) for _ in range(N)]

for n in range(N):
    new_line = ''
    for m in range(M):
        new_line += lattice[n][m] * K
    for i in range(K):
        print(new_line)