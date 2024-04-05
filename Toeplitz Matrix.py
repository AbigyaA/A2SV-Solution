class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n=len(matrix[0])
        for i in range(n-1):
            j=0
            while j < len(matrix):
                try:                    
                    if matrix[j][i] != matrix[j+1][i+1]:
                        return False
                except:
                    j+=1
                    continue
                j+=1
        return True
