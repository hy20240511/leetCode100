# 题目：螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    rows, columns = len(matrix), len(matrix[0])
    visited = [[False]*columns for _ in range(rows)]
    total = rows * columns
    order = [0] * total
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    row, column = 0, 0
    directionIndex = 0
    for i in range(total):
        order[i] = matrix[row][column]
        visited[row][column] = True
        nextRow, nextcolumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
        if not (0 <= nextRow < rows and 0 <= nextcolumn < columns and not visited[nextRow][nextcolumn]):
            directionIndex = (directionIndex+1) % 4
        row += directions[directionIndex][0]
        column += directions[directionIndex][1]
    return order
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))