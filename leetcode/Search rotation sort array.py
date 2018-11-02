class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        if not nums:return index
        i = 0
        j = len(nums) - 1
        if target == nums[i]:return i
        flag = True
        flgi = False
        flgj = False
        while flag and i < len(nums) - 1 and j > 0:
            if nums[i] == target:
                index = i
                flag = False
            elif nums[i] < target and nums[i+1] > nums[i]:
                i += 1
            else:
                flgi = True
            if nums[j] == target:
                index = j
                flag = False
            elif nums[j] > target and nums[j-1] < nums[j]:
                j -= 1
            else:
                flgj = True
            if flgi and flgj:
                break
        return index

if __name__ == '__main__':
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    target_nums = [4,5,6,7,0,1,2,3]
    for target in target_nums:
        print(solution.search(nums,target))