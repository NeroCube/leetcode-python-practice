'''
26近制轉10進制: AA = 1*26 + 1 ; BA = 2*26 + 1
ord('A') = 65
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for char in s:
            result = result*26 + ord(char) - 64
        return result