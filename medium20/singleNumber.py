'''
260. Single Number III

[題目]
找只有出現一次的數
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        one = set()
        two = set()
        for num in nums:
            if num not in one:
                one.add(num)
            else:
                two.add(num)
        return list(one - two)