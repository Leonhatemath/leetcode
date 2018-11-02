class Solution(object):
    def __init__(self):
        self.__dict__ = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,
                         'XC':90,'CD':400,'CM':900}
        self.list = ['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CM']
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        while s != '':
            if s[:2] in self.list:
                num += self.__dict__[s[:2]]
                s = s[2:]
            else:
                num += self.__dict__[s[0]]
                s = s[1:]
        return num

if __name__ == '__main__':
    solution = Solution()
    a = "IX"
    print(solution.romanToInt(a))