# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Same Tree

題目：
檢查兩棵樹是否是同一顆

想法：
- 如果兩個節點都是空的就回傳一樣
- 如果兩個節點都不是空的且值一樣
- 就繼續檢查是否兩邊一樣
- 直到節點都檢查完
- 只要沒有進到前面判斷即回傳不一樣


Time:  O(n)
Space: O()
'''
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None: 
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
