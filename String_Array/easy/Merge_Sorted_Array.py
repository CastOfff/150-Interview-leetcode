class Solution(object):
    def merge(self, nums1, m, nums2, n):
        idx_nums1 = m - 1 
        idx_nums2 =  n - 1
        idx_reverse = m + n - 1
        while idx_nums2 >= 0:
            if nums1[idx_nums1] > nums2[idx_nums2] and idx_nums1 >= 0 :
                nums1[idx_reverse] = nums1[idx_nums1]
                #nums1[idx_nums1] = nums2[idx_nums2]
                idx_nums1 -= 1
            else:
                nums1[idx_reverse] = nums2[idx_nums2]
                idx_nums2 -= 1
            idx_reverse -= 1
        return nums1
    
test_1 = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(test_1.merge(nums1, m, nums2, n))

