class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            if nums[0] < target:
                return 1
            else:
                return 0
        l = 0
        r = len(nums) - 1
        if nums[l] < target and nums[r] > target:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        elif nums[l] >= target:
            return 0
        elif nums[r] == target:
            return len(nums) - 1
        else:
            return len(nums)