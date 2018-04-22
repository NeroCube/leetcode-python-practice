'''
Replace Words

題目：
檢查句子中的字，從開頭開始看只要有符合字典中的片段整個字換成字典中的單詞。

想法：
- 將句子拆成單字
- 每個字從開頭開始看是否出現在字典中
- 是的話換掉

Time:  O(n)
Space: O(n)
'''
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