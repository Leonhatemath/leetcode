def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if 2 * nums[0] > target or 2 * nums[-1] < target:
            return []
        else:
            d = {}
            result = []
            for num in nums:
                if num + nums[-1] < target:continue
                if num in d.keys():
                    if [d[num], num] and [num, d[num]] not in result:
                        result.append([d[num], num])
                        del (d[num])
                    else:
                        continue
                else:
                    d[target - num] = num
            return result


nums = [11,15,20,-2,-7,11,15]
nums.sort()
target = -9
result = twoSum(nums=nums,target=target)
print(result)