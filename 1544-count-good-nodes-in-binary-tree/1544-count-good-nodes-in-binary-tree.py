# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self,node,maxVal):

        if not node:
            return 0

        res = 1 if node.val >= maxVal else 0

        maxVal=max(maxVal,node.val)

        res+=self.dfs(node.left,maxVal)
        res+=self.dfs(node.right,maxVal)

        return res

        

    
    
    def goodNodes(self, root: TreeNode) -> int:

                # VLR  arr=[root.val] , self.DFS(root.left) , self.DFS(root.right)
                # Keep the track of maximum :- maxi=max(maxi,root.val) 
                # 
        return self.dfs(root,root.val)


            
