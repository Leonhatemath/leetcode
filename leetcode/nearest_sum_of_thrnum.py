class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]+nums[1]+nums[2]
        else:
            nums.sort()
            result = nums[0] + nums[1] + nums[2]
            diff_value = abs(result - target)
            if diff_value == 0:return nums[0]+nums[1]+nums[2]
            solved = []
            for i in range(len(nums)-2):
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
                            return count
                        elif count > target:
                            if count - target < diff_value:
                                diff_value = count - target
                                result = count
                            k -= 1
                            while j < k and nums[k] == nums[k + 1]:
                                k -= 1
                        else:
                            if target - count < diff_value:
                                diff_value = target - count
                                result = count
                            j += 1
                            while j < k and nums[j] == nums[j - 1]:
                                j += 1
            return result

if __name__ == '__main__':
    solution = Solution()
    nums = [-1,2,1,-4]
    target = 1
    print(solution.threeSumClosest(nums,target))