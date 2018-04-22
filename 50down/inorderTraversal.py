# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
# 
'''
Binary Tree Inorder Traversal  

題目：
用中序走訪二元樹

想法：
- 中序走訪
- 走左子樹
- 走根
- 走右子樹
- 沒有可訪問的節點
- 返回前一個節點並印出結果(利用 stack 後進先出)

Time:  O()
Space: O()
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root, True))
                stack.append((root.left, False))
        return result
