'''
513. Find Bottom Left Tree Value

[題目]
在樹中找最深且最左邊的值

[思考]
最深優先權最高，依樣深選最左邊
DFS 我要記住目前最深的，還要知道我是該層最左邊的
BFS 由右至左，一層一層下去，最後一個值就是我們的答案
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