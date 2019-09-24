class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        
        for i in range(row):
            A[i] = A[i][::-1]
            for j in range(col):
                A[i][j] ^= 1
        return A
    
        #return [[1 ^ i for i in row[::-1]] for row in A]
