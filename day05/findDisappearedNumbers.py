class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        l=[]
        for i in range(1,len(nums)+1):
            if i not in nums:
                l+=[i]
        return l
