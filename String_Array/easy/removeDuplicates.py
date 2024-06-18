class Solution(object):
    def removeDuplicates(self, nums):  
        # n = len(nums) 
        # for i in range(n):
        #     j = i + 1
        #     while j < n: 
        #         if nums[i] == nums[j]:
        #             nums.pop(j)  
        #             n -= 1
        #         else:
        #             j+=1
        # return n
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
        """
        :type nums: List[int]
        :rtype: int
        """
test_1 = Solution()
nums = [1,1,2]
print(test_1.removeDuplicates(nums))