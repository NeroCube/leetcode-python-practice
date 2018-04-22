'''
countBits
'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [bin(index).count('1') for index in range(num+1)]
        