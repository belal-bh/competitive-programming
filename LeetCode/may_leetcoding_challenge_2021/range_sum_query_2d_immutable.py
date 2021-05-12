class NumMatrix:

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.cu_matrix = matrix.copy()
        for r in range(m):
            for c in range(n):
                cor, top, left = 0, 0, 0
                if r > 0:
                    top = self.cu_matrix[r-1][c]
                if c > 0:
                    left = self.cu_matrix[r][c-1]
                if r > 0 and c > 0:
                    cor = self.cu_matrix[r-1][c-1]
                self.cu_matrix[r][c] += top + left - cor

    def sumRegion(self, r1, c1, r2, c2):
        cor, top, left = 0, 0, 0
        if r1 > 0:
            top = self.cu_matrix[r1-1][c2]
        if c1 > 0:
            left = self.cu_matrix[r2][c1-1]
        if r1 > 0 and c1 > 0:
            cor = self.cu_matrix[r1-1][c1-1]
        return self.cu_matrix[r2][c2] - top - left + cor


# matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
#     1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# row1, col1, row2, col2 = 1, 2, 2, 4
# obj = NumMatrix(matrix)
# res = obj.sumRegion(row1, col1, row2, col2)
# print(res)
