class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        
        
        n = len(arr)
        k = k%n  
        
        
        
        arr[:n-k] = reversed(arr[:n-k])
        arr[n-k:] = reversed(arr[n-k:])
        
        
        
        
        arr.reverse()
        
        
           
            
            
            
        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        