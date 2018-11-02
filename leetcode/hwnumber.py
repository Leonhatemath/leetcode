class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = x
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        else:
            y = 0
            while x != 0:
                count = x % 10
                x //= 10
                y = y * 10 + count
            if flag == y:return True
            else:return False

solution = Solution()
for num in [121,-121,10]:
    if solution.isPalindrome(num):
        print('yes')
    else:
        print('no')