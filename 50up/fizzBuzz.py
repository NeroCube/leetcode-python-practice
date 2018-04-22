'''
Fizz Buzz 
'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        outputs = []
        for x in range(1, n + 1):
            result = ""
            if x % 3 == 0:
                result += "Fizz"
            if x % 5 == 0:
                result += "Buzz"
            if result is "":
                result = str(x)
            outputs.append(result)
        return outputs