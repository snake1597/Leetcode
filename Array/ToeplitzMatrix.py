class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
    
        # for i in range(1,len(matrix)):
        #     for j in range(1,len(matrix[0])):
        #         if matrix[i][j] != matrix[i-1][j-1]:
        #             return False
        # return True
        
        # for i in range(len(matrix)-1):
        #     if (matrix[i][0:len(matrix[0])-1] != 
        #         matrix[i+1][1:len(matrix[0])]):
        #         return False
        # return True
