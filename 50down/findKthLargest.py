'''
Kth Largest Element in an Array

題目：
找出第 k 個最大的元素

想法：
- 利用 Heap 回傳最小並且不改變父類別最小的特性
- 每個數變負數後，原本最大的數，會被先返回
- 跑 k 次迴圈取出，最後一個取出的就是第 k 個最大的元素
- 還原成正數

Time:  O()
Space: O()
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
        