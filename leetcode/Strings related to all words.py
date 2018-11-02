class Solution(object):
    def findAnswer(self, strstart, lenstr, lenword, lensubstr, s, times, ans):
        wordstart = strstart
        curr = {}
        while strstart + lensubstr <= lenstr:
            wd = s[wordstart:wordstart+lenword]
            wordstart += lenword
            if wd not in times:
                strstart = wordstart
                curr.clear()
            else:
                if wd in curr:
                    curr[wd] += 1
                else:
                    curr[wd] = 1
                if curr[wd] > times[wd]:
                    curr[wd] -= 1
                    cukeys = list(curr.keys())
                    windex = cukeys.index(wd)
                    count = 0
                    for delword in cukeys[:windex]:
                        count += curr[delword]
                        del curr[delword]
                    strstart += lenword * (count + 1)
                if wordstart-strstart == lensubstr:
                    ans.append(strstart)

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or words == []:
            return []
        lenstr = len(s)
        lenword = len(words[0])
        lensubstr = len(words)*lenword
        times = {}
        for wd in words:
            if wd in times:
                times[wd] += 1
            else:
                times[wd] = 1
        ans = []
        for i in range(min(lenword,lenstr-lensubstr+1)):
            self.findAnswer(i,lenstr,lenword,lensubstr,s,times,ans)
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    print(solution.findSubstring(s,words))