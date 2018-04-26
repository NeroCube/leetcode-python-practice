'''
535. Encode and Decode TinyURL

[題目]
短網址服務
'''
import random, string

class Codec:
    def __init__(self):
        self.__charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.__host = "http://tinyurl.com"
        self.__random_length = 6
        self.__dictionary = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
    
        :type longUrl: str
        :rtype: str
        """
        def randomUrl():
            randomchar = []
            for _ in range(self.__random_length):
                randomchar += self.__charSet[random.randint(0, len(self.__charSet)-1)]
            return "".join(randomchar)
        
        hashtag = randomUrl()
        while hashtag in self.__dictionary:
            hashtag = randomUrl()    
        
        self.__dictionary[hashtag] = longUrl
    
        return "{}/{}".format(self.__host, hashtag)
            
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        hashtag = shortUrl.split('/')[3]
        
        return self.__dictionary[hashtag]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))