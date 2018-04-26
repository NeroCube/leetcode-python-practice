'''
677. Map Sum Pairs

[題目]
在字典裡，搜尋的字是他的字首的單字，把他的值加總
'''
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = {}
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dictionary[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        for key in self.dictionary:
            if key.startswith(prefix):
                total += self.dictionary[key]
        return total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)