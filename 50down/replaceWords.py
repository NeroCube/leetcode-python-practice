class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        #從頭比對，如果在 dictset 就回傳切片
        dictset = set(dict)
        def replace(word):
            for i in range(len(word)):
                if word[:i] in dictset:
                    return word[:i]
            return word

        return ' '.join(map(replace, sentence.split()))