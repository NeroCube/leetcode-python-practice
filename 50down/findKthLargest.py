'''
利用 heapq.heappop 回傳最小的元素特性
'''
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for num in nums:
            heapq.heappush(heap, -num)
            
        for _ in range(k):
            res = heapq.heappop(heap)

        return res * -1
        