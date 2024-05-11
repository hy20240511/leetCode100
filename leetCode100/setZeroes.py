# 题目：矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    row, col = [False]*m, [False]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = col[j] = True
    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                matrix[i][j] = 0
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))
