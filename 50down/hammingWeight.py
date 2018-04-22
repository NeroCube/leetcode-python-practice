'''
Number of 1 Bits
題目：
將數轉成二進制時，整個數中有幾個1

想法：
- 將數轉成二進制
- 算有幾個1

Time:  O()
Space: O()   
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
