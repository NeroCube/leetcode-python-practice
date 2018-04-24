'''
406. Queue Reconstruction by Height
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