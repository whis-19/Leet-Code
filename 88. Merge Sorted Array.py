class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start from the end of nums1 and nums2
        p1, p2, p = m - 1, n - 1, m + n - 1

        # While there are elements to be processed in nums2
        while p2 >= 0:
            # If there are still elements in nums1 and the current element of nums1 is greater than the current element of nums2
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1