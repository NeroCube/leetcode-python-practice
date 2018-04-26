'''
406. Queue Reconstruction by Height

[題目]
按照每個人所說的自己前面看到，看到一樣或比自己高的人的狀況，恢復排序

[思考]
每個人會有盲點看不到比自己矮的人
所以誰說的一定是真的
最矮且說前面沒有人的
由矮到高排序，會沒辦法預期前面有幾個高的人錯誤
高的人不用在意前面有幾個比她矮的
所以最高說前面沒看到人的也是對的
由高到矮，高的說他看的比他高的人就是對的
'''

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        persons = sorted(people, key = lambda x:(-x[0], x[1]))
        result = []

        for _, person in enumerate(persons):
            result.insert(person[1], person)
        return result