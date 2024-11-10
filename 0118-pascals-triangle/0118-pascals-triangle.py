class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=[]
            
        for row in range(1,n+1):
            ans.append(self.generateRow(row))
        return ans
            
        
    def generateRow(self,row):
        ans=1
        ansRow=[1]
        
        for col in range(1,row):
            ans*=(row-col)
            ans//=col
            ansRow.append(ans)
        return ansRow
        
                
        
        
        
        