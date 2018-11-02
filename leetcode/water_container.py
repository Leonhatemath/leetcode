class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        contain = 0
        count = 0
        next_count = 0
        reverse_height = list(reversed(height))
        while count + next_count <= len(height) - 1:
            if height[count] <= reverse_height[next_count]:
                if contain <= height[count] * (len(height) - next_count - count - 1):
                    contain = height[count] * (len(height) - next_count - count - 1)
                count += 1
            else:
                if contain <= reverse_height[next_count] * (len(height) - next_count - count - 1):
                    contain = reverse_height[next_count] * (len(height) - next_count - count - 1)
                next_count += 1
        return contain


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))