'''
791. Custom Sort String

[題目]
按照給定 S 的字母順序，排序 T

[思路]
按照給定 S 的字母順序，則表示 Ｓ 中每個字母都有好號碼牌決定他的位置
取出 T 中每一字母問他，是否在 S 中有號碼牌
有的話我登記幾號
沒有的話我不確定會發到幾號，你先拿 -1，因為你排哪裡不重要
現在我們依據號碼牌來排隊

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
