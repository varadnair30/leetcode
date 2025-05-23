# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self,root,level,res):

        if not root:
            return
        
        if len(res)==level:
            res.append(root.val)

        self.func(root.right,level+1,res)
        self.func(root.left,level+1,res)


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res=[]

        self.func(root,0,res)
        return res



        