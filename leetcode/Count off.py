"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。
"""
class Solution:
    def count_off(self,s):
        if len(s) == 1:return '1' + s
        i = 0
        new_s = ''
        i_count = 1
        while i <= len(s) - 1:
            i += 1
            while i <= len(s) - 1 and s[i] == s[i-1]:
                i_count += 1
                i += 1
            new_s = new_s + str(i_count) + s[i-1]
            i_count = 1
        return new_s
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:return '1'
        s = '1'
        while n > 1:
            s = self.count_off(s)
            n -= 1
        return s

if __name__ == '__main__':
    solution = Solution()
    n = 4
    print(solution.countAndSay(n))
