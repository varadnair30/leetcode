from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if not root:
            return result
        
        nodesQueue=deque()
        nodesQueue.append(root)
        leftToRight=True

        
        

        while nodesQueue:

            size=len(nodesQueue)

            row=[0]*size  # List to store the values of nodes at the current level

            for i in range(size):

                node=nodesQueue.popleft()

                index = i if leftToRight else (size - 1 - i)

                row[index]= node.val

                if node.left:
                    nodesQueue.append(node.left)
                if node.right:
                    nodesQueue.append(node.right)


            leftToRight= not leftToRight

            result.append(row)

        return result



        