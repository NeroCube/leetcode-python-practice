'''
791. Custom Sort String
'''
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        sorted_string = sorted(T, key = lambda x: S.index(x) if x in S else -1)
        return ''.join(sorted_string)
