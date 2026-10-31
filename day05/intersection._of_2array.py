class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=[]
        for i in nums1:
            for j in nums2:
                if i==j and i not in res:
                    res+=[i]
        return res
