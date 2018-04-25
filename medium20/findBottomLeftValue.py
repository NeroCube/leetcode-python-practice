'''
513. Find Bottom Left Tree Value


BFS
'''
from Queue import Queue
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype int
        """
        queue = Queue()
        queue.put(root)
        node = None
        while not queue.empty():
            node = queue.get()
            if node.right:
                queue.put(node.right)
            if node.left:
                queue.put(node.left)

        return node.val