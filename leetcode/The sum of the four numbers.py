class Solution(object):
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums == [] or len(nums) < 3:
            pass
        else:
            solved = []
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
                        if count == target:
                            result.append([a, b, c])
                            j += 1
                            k -= 1
                            while j < k and nums[j] == nums[j - 1]: j += 1
                            while j < k and nums[k] == nums[k + 1]: k -= 1
                        elif count > target:
                            k -= 1
                            while j < k and nums[k] == nums[k + 1]: k -= 1
                        else:
                            j += 1
                            while j < k and nums[j] == nums[j - 1]: j += 1
        return result
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        solved = []
        result = []
        if len(nums) == 4 and sum(nums) == target:return [nums]
        for i in range(len(nums)-3):
            if nums[i] in solved:
                continue
            else:
                solved.append(nums[i])
                num_result = self.threeSum(nums[i+1:],target-nums[i])
                for num_list in num_result:
                    a = [nums[i]]
                    a.extend(num_list)
                    result.append(a)
        return result
