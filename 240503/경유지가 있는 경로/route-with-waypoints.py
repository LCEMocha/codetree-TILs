N, M, k = map(int, input().split())

matrix = [[0 for i in range(M)] for i in range(N)]

def to_layover(n,m):
    global matrix
    matrix[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            left = matrix[i][j-1] if j>0 else 0
            up = matrix[i-1][j] if i>0 else 0
            matrix[i][j] = left + up
    return matrix[n-1][m-1]

def to_destination(n,m):
    global matrix
    global N
    global M
    matrix[n][m] = 1
    for i in range(n,N):
        for j in range(m,M):
            if i == n and j == m:
                continue
            left = matrix[i][j-1] if j>0 else 0
            up = matrix[i-1][j] if i>0 else 0
            matrix[i][j] = left + up

if k == 0:
    to_layover(N,M)
    print(matrix[-1][-1])
else:
    n = (k // M) + 1 if k % M != 0 else k // M
    m = (k % M) if k % M != 0 else M
    to_layover_v = to_layover(n, m)
    to_destination(n-1, m-1)
    print(to_layover_v * matrix[-1][-1])