'''
Excel Sheet Column Number 

題目：
將 Excel 中的標題轉換成十進制的數字

想法：
- Excel 中 Z 代表26，AA 代表27，AB 代表28
- 所以是一個26近制變10進制的轉換(餘數定理)
- ord('A') = 65


Time:  O(n)
Space: O(1)
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