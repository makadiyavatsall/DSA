class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.Transpose(matrix)
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            for j in range(column // 2):
                matrix[i][j],matrix[i][column-1-j] = matrix[i][column-1-j],matrix[i][j]
                
    def Transpose(self,matrix):
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            for j in range(i+1,column):
                temp = matrix[i][j]
                matrix[i][j]= matrix[j][i]
                matrix[j][i]= temp
    

