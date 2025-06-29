from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):

        if not root: return ''

        s=''

        q=deque()

        q.append(root)

        while q:

            cur_node=q.popleft()
            if not cur_node:
                s+='null,'

            else:

                s+= str(cur_node.val) + ','

                q.append(cur_node.left)
                q.append(cur_node.right)

        return s

        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        tokens = data.split(',')
        if not tokens[0] or tokens[0] == "null":
            return None

        root = TreeNode(int(tokens.pop(0)))
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            # Be careful to avoid pop from empty list
            if tokens:
                left_val = tokens.pop(0)
                if left_val != "null" and left_val != "":
                    left_node = TreeNode(int(left_val))
                    node.left = left_node
                    q.append(left_node)
            if tokens:
                right_val = tokens.pop(0)
                if right_val != "null" and right_val != "":
                    right_node = TreeNode(int(right_val))
                    node.right = right_node
                    q.append(right_node)
        return root

            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))