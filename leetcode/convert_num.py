class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = True
        y = 0
        if x < 0:
            tag = True
        else:
            tag = False
        x = abs(x)
        while x != 0:
            count = x % 10
            x = x // 10
            if flag:
                y = count
            else:
                y = y * 10 + count
            flag = False
        if tag:
            y = -y
        if y < - 2 ** 31 or y > 2 ** 31 - 1:
            return 0
        else:
            return y

solution = Solution()
for num in [123,-123,120]:
    print(solution.reverse(num))