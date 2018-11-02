class Solution(object):
    """以每个字母为中心，考虑其左右是否相等来做"""
    def find(self,s,head_flag,tail_flag,hwzfc):
        while head_flag >= 0 and tail_flag <= len(s) - 1:
            if s[head_flag] == s[tail_flag]:
                head_flag -= 1
                tail_flag += 1
                if tail_flag - head_flag - 1 >= len(hwzfc):
                    hwzfc = s[head_flag + 1:tail_flag]
                else:
                    continue
            else:
                break
        return hwzfc

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 1
        if len(s) == 0:
            hwzfc = ''
        else:
            hwzfc = s[0]
        for count in range(len(s)):
            head_flag = count
            tail_flag = count
            if 0 < count < len(s)-1 and s[head_flag - 1] == s[tail_flag + 1]:
                hwzfc = self.find(s, head_flag - 1, tail_flag + 1, hwzfc)
            if 0 < count <= len(s)-1 and s[head_flag - 1] == s[tail_flag]:
                hwzfc = self.find(s, head_flag - 1, tail_flag, hwzfc)
            if 0 <= count < len(s)-1 and s[head_flag] == s[tail_flag + 1]:
                hwzfc = self.find(s, head_flag, tail_flag + 1, hwzfc)
            count += 1
        return hwzfc



solution = Solution()
for str in ['aa','ababd','cbbd','a','']:
    """这些情况基本包括所有"""
    print(solution.longestPalindrome(str))