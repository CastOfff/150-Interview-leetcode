class Solution(object):
    def removeElement(self, nums, val):
        new_nums = []
        for i in range(len(nums)):
            if nums[i] != val:
                new_nums.append(nums[i])
        return len(new_nums)
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """