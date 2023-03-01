class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)

        l = len(nums1)

        if l % 2 == 0:
            a = l // 2
            return (nums1[a-1] + nums1[a]) / 2
        else:
            a = l // 2
            return nums1[a]
        

        return 0