# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
    
        def dfs(node, current_path, current_sum):
            if not node:
                return
                
            # Add current node to path and update sum
            current_path.append(node.val)
            current_sum += node.val
            
            # Check if it's a leaf node and sum matches target
            if not node.left and not node.right and current_sum == targetSum:
                result.append(current_path.copy())
            
            # Continue DFS on left and right children
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            
            # Backtrack (remove current node from path when going up)
            current_path.pop()
        
        dfs(root, [], 0)
        return result

        