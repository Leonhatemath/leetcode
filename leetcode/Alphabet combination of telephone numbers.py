class Solution(object):
    def __init__(self):
        self.num2letter = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        for num in digits:
            num = int(num)
            num2letter = [letter for letter in self.num2letter[num]]
            if result == []:
                result = num2letter
            else:
                result = [y+x for x in num2letter for y in result]
        return result

if __name__ == '__main__':
    solution = Solution()
    nums = '23'
    print(solution.letterCombinations(nums))