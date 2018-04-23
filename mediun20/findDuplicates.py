'''
442. Find All Duplicates in an Array
'''
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictionary = {}
        result= []
        
        for num in nums:
            if num in dictionary:
                dictionary[num] = dictionary[num] + 1
                if dictionary[num] >= 2:
                    result.append(num)
            else:
                dictionary[num] = 1
        
        return result