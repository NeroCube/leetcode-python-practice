'''
Intersection of Two Arrays 

題目：
取兩個陣列重複的部分

想法：
- 兩個陣列做交集

Time:  O()
Space: O()
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return list(set(nums1) & set(nums2))