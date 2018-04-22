'''
Top K Frequent Elements 

題目：
找出在陣列中出現頻率大於等於 k 的元素

想法：
- 統計個元素個數
- 挑出個數大於等於 k 的元素

Time:  O(n)
Space: O(1)
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [key for key, _ in collections.Counter(nums).most_common(k)]
            