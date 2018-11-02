class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        sorted(nums1)
        length = len(nums1)
        index = length // 2
        if len(nums1) % 2 == 0:
            return (nums1[index-1] + nums1[index])/2
        else:
            return nums1[index]

solution = Solution()
print(solution.findMedianSortedArrays([1,2],[3]))