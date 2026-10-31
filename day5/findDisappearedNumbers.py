class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n=len(nums)
        l=[]
        for i in range(1,n+1):
            if i not in nums:
                l+=[i]
        return l
s=Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
