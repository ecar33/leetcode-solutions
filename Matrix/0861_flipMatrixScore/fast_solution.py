
def matrixScore(A):
    M, N = len(A), len(A[0])

    # If the first number in the row is 0, flip the row. 
    for i in range(M):
        if A[i][0] == 0:
            for j in range(N): A[i][j] ^= 1

    # If the count of 0 in the col is greater than the count of 1, flip the col. 
    for j in range(N):
        cnt = sum(A[i][j] for i in range(M))
        if cnt < M - cnt:
            for i in range(M): A[i][j] ^= 1

    # Sum the matrix
    return sum(int(''.join(map(str, A[i])), 2) for i in range(M))


grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(matrixScore(grid))