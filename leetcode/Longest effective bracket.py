class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lefbrack = '('
        rigbrack = ')'
        stack = []
        lglen = 0
        index = 0
        for i in range(len(s)):
            if s[i] == lefbrack:
                stack.append(i)
            elif s[i] == rigbrack:
                if len(stack) == 0:
                    index = i + 1
                else:
                    stack.pop()
                    if len(stack) == 0:
                        lglen = max(lglen,i+1-index)
                    else:
                        lglen = max(lglen,i-stack[-1])
            else:
                return lglen
        return lglen

if __name__ == '__main__':
    solution = Solution()
    for s in ['()(()','())(())']:
        print(solution.longestValidParentheses(s))