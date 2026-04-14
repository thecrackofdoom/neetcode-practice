class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == len(matrix[0]):
            for r in range(len(matrix)):
                for c in range(r, len(matrix[0])):
                    if r != c:
                        print(matrix[r][c], matrix[c][r])
                        matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                        
            return matrix
        else:
            mat = []
            for i in range(len(matrix[0])):
                mat.append([])
                for j in range(len(matrix)):
                    mat[i].append(matrix[j][i])
                    print(mat)
            return mat