# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def SameTree(self,p,q):

        if not q or not p:
            return p==q

        
        
        return (p.val==q.val) and self.SameTree(p.left,q.left) and self.SameTree(p.right,q.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False

        if self.SameTree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or (self.isSubtree(root.right,subRoot)))






        
        