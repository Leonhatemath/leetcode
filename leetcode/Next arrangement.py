class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return nums
        count = 0
        for i in range(len(nums)):
            i += 1
            if i < len(nums):
                a = nums[-i]
                b = nums[-i - 1]
                count += 1
                if a > b:
                    break
            else:break
        sub_nums = nums[-count:]
        sub_nums.sort()
        for i in range(len(sub_nums)):
            a = sub_nums[i]
            b = nums[-count-1]
            if a > b:
                nums[-count-1] = a
                sub_nums[i] = b
                break
        nums[-count:] = sub_nums
        return nums

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1]
    print(solution.nextPermutation(nums))