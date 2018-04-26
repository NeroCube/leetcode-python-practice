'''
540. Single Element in a Sorted Array

[題目]
每個數都會出現兩次，找出唯一一個單獨的數

[思考]
每個數都會出現兩次
希望自己可以消滅自己
邏輯異或

'''


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