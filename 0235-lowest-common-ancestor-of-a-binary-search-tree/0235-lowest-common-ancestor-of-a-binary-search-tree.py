# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        '''if not root:
            return None

        cur=root.val

        if cur < p.val and cur < q.val:                            # if both of them lie on the right
            return self.lowestCommonAncestor(root.right,p,q)       # lets go to the right

        if cur > p.val and cur > q.val:                            # if both of them lie on the left
            return self.lowestCommonAncestor(root.left,p,q)        # lets go to the left

        return root                                                # if can't determine where to go ,  its firstpoint of intersection
        '''
        if not root:
            return None

        

        while root:
            cur=root.val
            if cur < p.val and cur < q.val:
                root=root.right

            elif cur > p.val and cur > q.val:
                root=root.left

            else:
                return root
