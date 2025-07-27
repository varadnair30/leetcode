# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self,root):

        return not root.left and not root.right

    def addLeftBoundary(self,root,res):

        cur=root.left

        while cur:

            if not self.isLeaf(cur): res.append(cur.val)

            if cur.left: cur=cur.left

            else: cur=cur.right

    def addRightBoundary(self,root,res):

        cur=root.right
        temp=[]

        while cur:

            if not self.isLeaf(cur): temp.append(cur.val)

            if cur.right: cur=cur.right

            else: cur=cur.left

        for i in range(len(temp)-1,-1,-1):

            res.append(temp[i])

    def addLeaves(self,root,res):
        if self.isLeaf(root): 
            res.append(root.val)
            return

        if root.left:

            self.addLeaves(root.left,res)

        if root.right:

            self.addLeaves(root.right,res)

    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:


        res=[]

        if not root: return res

        if not self.isLeaf(root):
            res.append(root.val)

        self.addLeftBoundary(root,res)
        self.addLeaves(root,res)
        self.addRightBoundary(root,res)

        return res





        