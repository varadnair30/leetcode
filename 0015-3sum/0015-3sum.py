class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        n=len(arr)
        res=[]
        arr.sort()
        
        for i in range(n):
            # remove the duplicates
            
            if i!=0 and arr[i]==arr[i-1]:
                continue
            j=i+1
            k=n-1
            
            while j<k:
                total_sum=arr[i]+arr[j]+arr[k]
                if total_sum<0:
                    j+=1
                elif total_sum>0:
                    k-=1
                else:
                    temp=[arr[i],arr[j],arr[k]]
                    res.append(temp)
                    j+=1
                    k-=1
                    while j<k and arr[j]==arr[j-1]:   #skip the duplicates
                        j+=1
                    while j<k and arr[k]==arr[k+1]:   #skip the duplicates
                        k-=1
                    
        return res    
                        
                        
        
        
        