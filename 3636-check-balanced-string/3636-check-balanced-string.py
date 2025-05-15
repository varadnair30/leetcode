class Solution:
    def isBalanced(self, num: str) -> bool:

        eve_sum,odd_sum=0,0
        eve_index,odd_index=0,1

        while odd_index<len(num):

            

            odd_sum+=int(num[odd_index])

            

            odd_index+=2

        while eve_index<len(num):

            eve_sum+=int(num[eve_index])

            

            eve_index+=2

            

        return eve_sum==odd_sum

        
            
        