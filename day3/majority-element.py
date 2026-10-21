class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        maj=n//2
        for i in nums:
            c=0
            for j in nums:
                if i==j:
                    c+=1
        if c>maj:
            return i
soln=Solution()
print(soln.majorityElement([3,2,3]))
