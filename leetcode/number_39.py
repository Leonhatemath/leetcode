"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
"""
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        # candidates.sort() 先假设是排好序的数组
        for num in candidates:
            if target % num == 0:
                result.append([num]*(target//num))
            else:
                if num > target:
                    return result
                target -= num
                next_result = self.combinationSum(candidates,target)
                if next_result != []:
                    for result_list in next_result:
                        result_list.append(num)
                        result.append(result_list)
        return result

if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(solution.combinationSum(candidates,target))