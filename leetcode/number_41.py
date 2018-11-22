class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            while nums[i] > 0 and nums[i] <= length and nums[nums[i]-1] != nums[i]:
                #该数大于0，该数小于数组长度，该数不在本应该在的位置上,则进行交换
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1

if __name__ == '__main__':
    solution = Solution()
    nums = [3,4,-1,1]
    print(solution.firstMissingPositive(nums))