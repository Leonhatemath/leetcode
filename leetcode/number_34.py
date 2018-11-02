class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:return [-1,-1]
        if len(nums) == 1 and target == nums[0]:return [0,0]
        if len(nums) == 2:
            if nums[0] == nums[1] == target:return[0,1]
            elif nums[0] == target:return[0,0]
            elif nums[1] == target:return[1,1]
        l = 0
        r = len(nums) - 1
        while l <= r :
            mid = (r+l)//2
            if nums[l] <= target and nums[r] >= target:
                if nums[mid] == target:
                    l = mid
                    r = mid
                    while l - 1 >= 0 and nums[l-1] == nums[l]:
                        l -= 1
                    while r + 1 <= len(nums) - 1 and nums[r+1] == nums[r]:
                        r += 1
                    return [l,r]
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            else:
                return [-1,-1]
        return [-1,-1]

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    target = 1
    print(solution.searchRange(nums,target))