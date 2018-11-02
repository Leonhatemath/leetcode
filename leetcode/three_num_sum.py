class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums == [] or len(nums) < 3:
            pass
        else:
            solved = []
            nums.sort()
            for i in range(len(nums)):
                a = nums[i]
                if a in solved:
                    continue
                else:
                    solved.append(a)
                    j = i + 1
                    k = len(nums) - 1
                    while j < k:
                        b = nums[j]
                        c = nums[k]
                        count = a + b + c
                        if count == 0:
                            result.append([a, b, c])
                            j += 1
                            k -= 1
                            while j < k and nums[j] == nums[j - 1]: j += 1
                            while j < k and nums[k] == nums[k + 1]: k -= 1
                        elif count > 0:
                            k -= 1
                            while j < k and nums[k] == nums[k + 1]: k -= 1
                        else:
                            j += 1
                            while j < k and nums[j] == nums[j - 1]: j += 1
        return result