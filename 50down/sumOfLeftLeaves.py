# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Sum of Left Leaves 
題目：
加總整棵樹左邊的子葉

想法：
- 沒有樹回傳0
- 判斷是不是葉
- 左葉回傳原本的值，右葉回傳零
- 並在方入葉的時，紀錄是不是左邊
- 遞迴

Time:  O(n)
Space: O()
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
        