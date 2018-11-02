class Solution(object):
    def __init__(self):
        self.dict = {'(':')','[':']','{':'}'}
        self.list = ['(']
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:return False
        if len(s) == 2 and s[1] == self.dict[s[0]] :return True
        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):return False
        for i in range(0,len(s)-1,2):
            if s[:i]

        if s[:len(s)//2].count('(') <= s.count(')') or s[:len(s)//2].count('[') <= s.count(']') or s[:len(s)//2].count('{') <= s.count('}'):return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s = "}{"
    if solution.isValid(s):
        print('True')
    else:
        print('False')