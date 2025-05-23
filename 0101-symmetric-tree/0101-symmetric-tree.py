# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def travHelp(self,root,left,right):
        if not left or not right:
            return left==right

        if left.val!=right.val:
            return False

        return self.travHelp(root,left.left,right.right) and self.travHelp(root,left.right,right.left)

    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:




        return self.travHelp(root,root.left,root.right)







        