class Solution(object):
    def removeDuplicates(self, nums):
        k=1
        nums.append("")
        for i in range(1,len(nums)-1):
            if nums[i-1] != nums[i] or nums[i] != nums[i+1]:
                nums[k] = nums[i]
                k+=1
        return k
        """
        :type nums: List[int]
        :rtype: int
        """
test_1 = Solution()
nums = [1,1,1,2,2,3]
print(test_1.removeDuplicates(nums))