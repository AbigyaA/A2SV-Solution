class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        first=matrix[0]
        output=[]        
        for i in range(len(first)):
            t=[]
            t.append(first[i])
            for j in range(1,len(matrix)):
                t.append(matrix[j][i])
            output.append(t)
        return output
