# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inMap = {val: idx for idx, val in enumerate(inorder)}
        
        # Call the private helper function to recursively build the tree
        root = self.HelperbuildTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)
        
        return root

    def HelperbuildTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        if preStart > preEnd or inStart > inEnd:
            return None

        # Create a new TreeNode with value at the current preorder index
        root = TreeNode(preorder[preStart])

        # Find the index of the current root value in the inorder traversal
        inRoot = inMap[root.val]

        # Calculate the number of elements in the left subtree
        numsLeft = inRoot - inStart

        # Recursively build the left subtree
        root.left = self.HelperbuildTree(preorder, preStart + 1, preStart + numsLeft,
                                    inorder, inStart, inRoot - 1, inMap)

        # Recursively build the right subtree
        root.right = self.HelperbuildTree(preorder, preStart + numsLeft + 1, preEnd,
                                     inorder, inRoot + 1, inEnd, inMap)

        # Return the current root node
        return root
        