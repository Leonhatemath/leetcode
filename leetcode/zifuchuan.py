class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        num = 0
        for letter in s:
            chstr = letter
            for next_letter in s[num + 1:]:
                if next_letter not in chstr:
                    chstr = chstr + next_letter
                else:
                    if len(chstr) > count:count = len(chstr)
                    break
            if chstr == s or chstr == s[num:] or count > len(s)-num:
                if len(chstr) > count: count = len(chstr)
                break
            num += 1
        return count

s = 'aab'
solution = Solution()
print(solution.lengthOfLongestSubstring(s))