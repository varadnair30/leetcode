from collections import defaultdict,deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        if not root:
            return 0

        max_width = 0  # Stores the maximum width encountered

        # Deque for BFS traversal; each element is (node, position_index)
        queue = deque()
        queue.append((root, 0))  # Start with the root at position 0

        while queue:
            size = len(queue)             # Number of nodes at this level
            min_index = queue[0][1]       # Index of the first node in this level

            # 'first' and 'last' will hold the normalized positions of the first and last nodes
            first, last = None, None

            for i in range(size):
                node, idx = queue.popleft()

                # Normalize index to avoid integer overflow for deep trees
                idx -= min_index

                # For the first node at this level
                if i == 0:
                    first = idx
                # For the last node at this level
                if i == size - 1:
                    last = idx

                # Enqueue left child with its position in a full binary tree
                if node.left:
                    queue.append((node.left, 2 * idx + 1))
                # Enqueue right child with its position in a full binary tree
                if node.right:
                    queue.append((node.right, 2 * idx + 2))

            # Calculate width at this level and update maximum width
            level_width = last - first + 1
            max_width = max(max_width, level_width)

        # Return the maximum width found
        return max_width


