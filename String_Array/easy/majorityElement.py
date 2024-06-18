class Solution(object):
    def majorityElement(self, nums):
        '''The First'''
        # nums.sort()
        # k = nums[0]
        # count = 1
        # countMax = 1
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         count+=1
        #         if count > countMax:
        #             k = nums[i]
        #             countMax = count
        #     else: count = 1
        # return k
        ''' the Second'''
        # nums.sort()
        # return nums[len(nums)/2]
        ''' the Third and FINAL'''
        k = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                k = nums[i]
            if k == nums[i]:
                count += 1
            else: count -= 1
        return k

            
        """
        :type nums: List[int]
        :rtype: int
        """
test_1 = Solution()
nums = [2,2,1,1,1,2,2]
print(test_1.majorityElement(nums))