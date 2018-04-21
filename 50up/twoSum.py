class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i, num in enumerate(nums):
            if target - num in result:
                return [result[target - num], i]
            result[num] = i
                
        
            
        