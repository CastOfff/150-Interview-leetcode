class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums1 = nums[-k:]
        nums2 = nums[:-k]
        nums[:] = nums1 + nums2
        return nums
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
test_1 = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(test_1.rotate(nums, k))