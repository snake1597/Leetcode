class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag = True
        current = A[0]
        if A[-1] > A[0]:
            for i in range(1,len(A)):
                if A[i] >= current:
                    current = A[i]
                    flag = True
                else:
                    flag = False
                    break
        else:
            for i in range(1,len(A)):
                if A[i] <= current:
                    current = A[i]
                    flag = True
                else:
                    flag = False 
                    break
        return flag
