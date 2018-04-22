'''
Two Sum II - Input array is sorted  

題目：
尋找 numbers 中兩個可以組成 target 的元素位置

想法：
- 走訪每個 numbers 元素
- 建立一個 dict 
- 將 target 減掉取出的元素得到另外一半元素，並檢查另外一半元素是否在 dict 中
- 存在時則找到需要的兩個數，回傳其個別在 numbers 陣列中的索引，結束迴圈
- 否則將當前取出的元素存入 dict

Time:  O(n)
Space: O(n)
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i, num in enumerate(numbers):
            if target - num in dictionary:
                return [(dictionary[target - num]+1), (i+1)]
            dictionary[num] = i