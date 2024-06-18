class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        count = 0
        while count < n:
            if nums[count] == val:
                for i in range(count, n-1):
                    nums[i] = nums[i+1]
                n -= 1
            else:
                count += 1
        return n
    
test_1 = Solution()
nums = [3,2,2,3]
val = 3
print(test_1.removeElement(nums, val))


"""
:type nums: List[int]
:type val: int
:rtype: int
"""