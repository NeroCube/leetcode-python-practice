class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for index in range(len(nums)):
            result ^=  nums[index]
        
        return result