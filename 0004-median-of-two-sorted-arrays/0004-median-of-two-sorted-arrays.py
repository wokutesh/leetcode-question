class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finlist=nums1+nums2
        finlist=sorted(finlist)
        if len(finlist)%2!=0:
            return finlist[len(finlist)//2]
        else:
            return (finlist[len(finlist)//2]+ finlist[(len(finlist)//2)-1])/2