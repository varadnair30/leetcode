class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        rows,cols=len(mat),len(mat[0])
        cnt_mx,index=0,0

        for i in range(rows):
            cnt_ones=0
            for j in range(cols):
                if mat[i][j]==1:
                    cnt_ones+=1

            
            if cnt_ones>cnt_mx:
                cnt_mx=cnt_ones
                index=i

        return [index,cnt_mx]
        
    



        