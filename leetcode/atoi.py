class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        try:
            word = str.split()[0]
            if word[0] not in '-+0123456789':
                return 0
            else:
                new_word = word[0]
                for letter in word[1:]:
                    if letter not in '1234567890':
                        break
                    else:new_word += letter
                word = int(new_word)
                if word < - 2 ** 31:
                    word = - 2 ** 31
                elif word > 2 ** 31 - 1:
                    word = 2 ** 31 - 1
                else:
                    pass
                return word
        except:return 0


solution = Solution()
for string in ['-5-','42','    -42','4193 with words','words and 987','-91283472332','3.14159','']:
    print(solution.myAtoi(string))