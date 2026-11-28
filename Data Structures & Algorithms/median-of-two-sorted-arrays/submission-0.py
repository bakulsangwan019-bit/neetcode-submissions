class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        lef1 = 0
        lef2 = 0

        total = len(nums1) + len(nums2)

        merge = []

        while (len(merge) < total//2 + 1):

            if lef1 >= len(nums1):
                merge.append(nums2[lef2])
                lef2 += 1

            elif lef2 >= len(nums2):
                merge.append(nums1[lef1])
                lef1 += 1

            elif nums1[lef1] <= nums2[lef2]:
                merge.append(nums1[lef1])
                lef1 += 1

            else:
                merge.append(nums2[lef2])
                lef2 += 1

        if total % 2 == 0:
            median = (merge[total//2 - 1] + merge[total//2]) / 2
        else:
            median = merge[total//2]

        return median 