class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        count = 0
        flag = True
        new_string = {}
        string = ''
        for letter in s:
            if len(new_string) <= count:
                new_string[count] = letter
            else:
                new_string[count] += letter
            if flag:
                count += 1
            else:
                count -= 1
            if count == numRows - 1:
                flag = False
            elif count == 0:
                flag = True
        for word in new_string.values():
            string += word
        return string

solution = Solution()
string = 'PAYPALISHIRING'
for num in [3,4]:
    print(solution.convert(string,num))