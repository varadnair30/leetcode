# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def valid(self,root, minVal,maxVal):

        if not root: return True

        if minVal>=root.val or root.val>=maxVal:
            return False

        return self.valid(root.left,minVal,root.val) and self.valid(root.right,root.val,maxVal)

         


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.valid(root,float('-inf'),float('inf')) 




        














        