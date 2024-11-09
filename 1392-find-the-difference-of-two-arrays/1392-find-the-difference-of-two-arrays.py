class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:    
        s_list=set(nums1)
        s_list2=set(nums2)
        res1=[]
        res2=[]
        ans=[]
        for i in s_list:
            if i not in s_list2:
                res1.append(i)

        for j in s_list2:
            if j not in s_list:
                res2.append(j)

        ans.append(res1)
        ans.append(res2)
        return ans

        