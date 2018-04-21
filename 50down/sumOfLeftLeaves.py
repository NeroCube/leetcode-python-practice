# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
遞迴：左邊的回傳原本的數，右邊的回傳零，根的值設為左右相加，
'''
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumOfLeftLeavesTool(root, is_left):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if is_left else 0
            return sumOfLeftLeavesTool(root.left, True) + sumOfLeftLeavesTool(root.right, False)
        
        return sumOfLeftLeavesTool(root, False)
        